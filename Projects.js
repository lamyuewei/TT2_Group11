import React from "react";
import AddExpense from "./AddExpense";
import IndivProject from "./IndivProject";

const Projects = ({ projects, onClick, onDelete }) => {
  return (
    <>
      {projects.map((cat) => (
        <IndivProject
          onDelete={onDelete}
          key={cat.id}
          project={cat}
          onClick={onClick}
        />
      ))}
    </>
  );
};

export default Projects;
