const { Sequelize, DataTypes } = require("sequelize");

const sequelize = new Sequelize("postgres", "postgres", "root", {
  host: "localhost",
  dialect: "postgres",
});

const User = sequelize.define(
  "user",
  {
    userId: {
      type: DataTypes.STRING,
      allowNull: false,
      primaryKey: true,
    },
    isPaused: {
      type: DataTypes.BOOLEAN,
      defaultValue: false,
    },
    maxTimeAllowed: {
      type: DataTypes.INTEGER,
      defaultValue: 60,
    },
    currentTime: {
      type: DataTypes.INTEGER,
      allowNull: true,
      defaultValue: 0,
    },
    pauseMessage: {
      type: DataTypes.STRING,
      allowNull: true,
      defaultValue: null,
    },
  },
  {
    tableName: "users",
    timestamps: false,
    createdAt: false,
    updatedAt: false,
  }
);

// Create the "user" table in the database
sequelize
  .sync({ force: true })
  .then(() => console.log("User table created successfully"))
  .catch((error) => console.log("Error creating user table: ", error));

// Export the User model
module.exports = { User };
