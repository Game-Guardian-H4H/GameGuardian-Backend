const { Sequelize, DataTypes } = require("sequelize");
const sequelize = new Sequelize("postgres", "postgres", "root", {
  dialect: "postgres",
  host: "localhost",
});

const User = sequelize.define("user", {
  userId: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  isPaused: {
    type: DataTypes.BOOLEAN,
    defaultValue: false,
  },
  maxTimeAllowed: {
    type: DataTypes.INTEGER,
    defaultValue: 20,
  },
});

// Define a function to create and save a user to the database
async function createUser(userId, isPaused, maxTimeAllowed) {
  const user = await User.create({
    userId: userId,
    isPaused: isPaused,
    maxTimeAllowed: maxTimeAllowed,
  });

  console.log(`Created user with id ${user.userId}`);
}

// Create an array of users to add to the database
const users = [
  { userId: "user1", isPaused: false, maxTimeAllowed: 20 },
  { userId: "user2", isPaused: false, maxTimeAllowed: 20 },
  { userId: "user3", isPaused: true, maxTimeAllowed: 10 },
  { userId: "user4", isPaused: false, maxTimeAllowed: 20 },
  { userId: "user5", isPaused: true, maxTimeAllowed: 15 },
  { userId: "user6", isPaused: false, maxTimeAllowed: 30 },
  { userId: "user7", isPaused: false, maxTimeAllowed: 20 },
  { userId: "user8", isPaused: true, maxTimeAllowed: 25 },
  { userId: "user9", isPaused: false, maxTimeAllowed: 20 },
  { userId: "user10", isPaused: true, maxTimeAllowed: 30 },
];

// Add each user to the database in a loop
async function addUsers() {
  for (const user of users) {
    await createUser(user.userId, user.isPaused, user.maxTimeAllowed);
  }
}

// Call the addUsers function to add the users to the database
addUsers();
