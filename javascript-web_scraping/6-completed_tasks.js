#!/usr/bin/node
// This script computes the number of tasks completed by user id.
// The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
// This script only prints users with completed task
// It uses the module request
const reqNumTasks = require('request');
reqNumTasks(process.argv[2], function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    let completedTasks = {};
    todos.forEach((todo) => {
      if (todo.completed && completedTasks[todo.userId] === undefined) {
        completedTasks[todo.userId] = 1;
      } else if (todo.completed) {
        completedTasks[todo.userId] += 1;
      }
    });
    console.log(completedTasks);
  }
});
