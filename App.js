import {
  BrowserRouter as Router,
  Route,
  Routes,
  useNavigate,
} from "react-router-dom";
import React, { useState, useEffect, useCallback } from "react";

import Login from "./Components/Login";
import Header from "./Components/Header";
import Main from "./Components/Main";

function App() {
  const userDetails = [
    { username: "user101", password: "123456" },
    { username: "Second", password: "Hello" },
  ];

  const onCheck = () => {
    console.log("");
  };
  // const history = useNavigate();
  // useCallback(() => history.push("/"), [history]);

  return (
    <div className="container">
      <Router>
        <Routes>
          <Route
            path="/"
            element={
              <>
                <Header />
                <Login
                  password={userDetails[0].password}
                  username={userDetails[0].username}
                  onClick={onCheck}
                />
              </>
            }
          />

          <Route path="/main" element={<Main />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
