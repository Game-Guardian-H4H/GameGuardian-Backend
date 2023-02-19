const express = require("express");
const { Op } = require("sequelize");
const { User } = require("./models");

const app = express();
const END_POINT = "/api/v1";

app.get(`${END_POINT}/users`, async (req, res) => {
  try {
    const users = await User.findAll();

    res.json(users);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: "Internal server error" });
  }
});

// Define an endpoint to get a specific user by their userId
app.get(`${END_POINT}/users/:userId`, async (req, res) => {
  try {
    // Extract the userId from the request parameters
    const { userId } = req.params;

    // Query the "user" table for the user with the given userId
    const user = await User.findOne({ where: { userId } });

    // If the user is found, send it as a JSON response
    if (user) {
      res.json(user);
    } else {
      res.status(404).json({ message: "User not found" });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: "Internal server error" });
  }
});

app.use(express.json());

app.post(`${END_POINT}/users/create`, async (req, res) => {
  try {
    const { body } = req;
    const { userId } = body || {};

    // Create a new user with the provided parameters
    const newUser = await User.create({
      userId: userId,
      isPaused: false,
      pauseMessage: "",
      maxTimeAllowed: 60,
      currentTime: 0,
    });

    // Send the new user as a JSON response
    res.json(newUser);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: "Internal server error" });
  }
});

app.post(`${END_POINT}/users/:userId/pause`, async (req, res) => {
  try {
    // Extract the userId from the request parameters
    const { userId } = req.params;

    // Extract the isPaused and pauseMessage properties from the request body
    const { isPaused, pauseMessage } = req.body;
    console.log(isPaused, pauseMessage);

    // Update the user with the given userId
    const result = await User.update(
      { isPaused, pauseMessage },
      { where: { userId } }
    );

    // If the user is found and updated, send a success message as a JSON response
    if (result[0]) {
      res.json({ message: "User updated successfully" });
    } else {
      res.status(404).json({ message: "User not found" });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: "Internal server error" });
  }
});

app.post(`${END_POINT}/users/:userId/pause/currentTime`, async (req, res) => {
  try {
    // Extract the userId from the request parameters
    const { userId } = req.params;

    // Extract the isPaused and pauseMessage properties from the request body
    const { currentTime } = req.body;

    // Update the user with the given userId
    const result = await User.update({ currentTime }, { where: { userId } });

    // If the user is found and updated, send a success message as a JSON response
    if (result[0]) {
      res.json({ message: "User updated successfully" });
    } else {
      res.status(404).json({ message: "User not found" });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: "Internal server error" });
  }
});

app.post(`${END_POINT}/users/:userId/maxTimeAllowed`, async (req, res) => {
  try {
    const { userId } = req.params;
    const { maxTimeAllowed } = req.body;

    // Find the user by userId
    const user = await User.findOne({ where: { userId } });

    if (user) {
      // Update the maxTimeAllowed property for the user
      user.maxTimeAllowed = maxTimeAllowed;
      await user.save();

      res.json({ message: "User updated successfully" });
    } else {
      res.status(404).json({ message: "User not found" });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: "Internal server error" });
  }
});

app.get(`${END_POINT}/server/healthCheck`, async (req, res) => {
  try {
    // Check the health status of the Postgres connection
    res.status(200).json({ health_status: "green" });
  } catch (error) {
    console.error(error);
    res.status(500).json({ health_status: "red" });
  }
});

// Start the Express app
app.listen(3000, () => {
  console.log("App listening on port 3000");
});
