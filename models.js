const { Sequelize, DataTypes } = require("sequelize");

// Define a new Sequelize instance with a connection to a database
const sequelize = new Sequelize("postgres", "postgres", "root", {
  host: "localhost",
  dialect: "postgres",
});

// Define a User model
const User = sequelize.define(
  "User",
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
    pauseMessage: {
      type: DataTypes.STRING,
      defaultValue: "",
    },
    maxTimeAllowed: {
      type: DataTypes.INTEGER,
      defaultValue: 60,
    },
    currentTime: {
      type: DataTypes.INTEGER,
      defaultValue: 0,
    },
  },
  {
    tableName: "users",
    timestamps: false,
    createdAt: false,
    updatedAt: false,
  }
);

// Export the User model
module.exports = { User };
