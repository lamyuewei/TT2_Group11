import { BrowserRouter as Router, Route, NavLink } from "react-router-dom";
import React, { useState, useEffect } from "react";

import Login from "./Components/Login";
import Header from "./Components/Header";

function App() {
  const userDetails = [
    { Username: "Hello", Pass: "Hello" },
    { Username: "Second", Pass: "Hello" },
  ];

  const onCheck = () => {
    console.log("Clicked");
  };

  return (
    <div className="container">
      <Header />
      <Login userDetails={userDetails[0]} onClick={onCheck} />
    </div>
  );
}

export default App;
