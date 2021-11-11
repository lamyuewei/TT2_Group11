import React, { useState } from "react";
import Projects from "./Projects";
import { Route, Redirect } from "react-router-dom";
import AddExpense from "./AddExpense";

function Main() {
  const [userProjects, setuserProjects] = useState([
    {
      id: 1,
      name: "Jacky",
      appointment: "Project Lead",
      projectName: "SWT",
      budget: 80000,
      description: "Smart Watch Tracker",
      expenseName: "Server Maintenance",
      expenseDescription:
        "Server maintenance and upgrading work to incorporate BC plans",
      expenseAmount: 30000,
    },
    {
      id: 2,
      name: "Jane",
      appointment: "Project Manager",
      projectName: "ULS",
      budget: 11000,
      description: "Upgrade Legacy System",
      expenseName: "Consultant",
      expenseDescription: "Consultancy services for integration work",
      expenseAmount: 10000,
    },
    {
      id: 3,
      name: "Tom",
      appointment: "Project Manager",
      projectName: "",
      budget: 0,
      description: "",
      expenseName: "",
      expenseDescription: "",
      expenseAmount: 0,
    },
    {
      id: 4,
      name: "Helen",
      appointment: "Project Manager",
      projectName: "RTF",
      budget: 12000,
      description: "Realtime Face Recogniton",
      expenseName: "",
      expenseDescription: "",
      expenseAmount: 0,
    },
    {
      id: 5,
      name: "Mark",
      appointment: "Senior Project Manager",
      projectName: "",
      budget: 0,
      description: "",
      expenseName: "",
      expenseDescription: "",
      expenseAmount: 0,
    },
  ]);

  const onDelete = (id) => {
    setuserProjects(userProjects.filter((project1) => project1.id != id));
  };

  return (
    <div>
      <h1>This is the main page</h1>
      <a href="/">Go back to log in page</a>
      <Projects projects={userProjects} onDelete={onDelete} />
    </div>
  );
}

export default Main;
