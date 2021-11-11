import React from "react";
import AddExpense from "./AddExpense";

const IndivProject = ({ project, onDelete }) => {
  var displayFields = false;
  const onAdd = () => {
    displayFields = !displayFields;
    console.log(displayFields);
  };

  return (
    <div>
      <h2
        style={{ color: "white", backgroundColor: "grey", paddingLeft: "20px" }}
      >
        {project.name}
      </h2>
      <p>Project Name: {project.projectName}</p>
      <p>Budget: ${project.budget}</p>
      <p>Project Description: {project.description}</p>
      <p>Expense Name: {project.expenseName}</p>
      <p>Expense Description: {project.expenseDescription}</p>
      <p>Expense Amount: ${project.expenseAmount}</p>
      <button className="btn" onClick={onAdd}>
        Add
      </button>
      <button className="btn">Edit</button>
      <button className="btn" onClick={() => onDelete(project.id)}>
        Remove
      </button>
    </div>
  );
};

export default IndivProject;
