import React from "react";
import "./App.css";

function App() {
  return (
    <div className="App">
      <div className="black-nav">
        <div className="nav-left">이것저것 환율 계산기</div>
        <div className="nav-right">
          <a
            href="https://github.com/PzaThief/egg-exchanger"
            target="_blank"
            style={{ color: "inherit", textDecoration: "inherit" }}
          >
            코드 보러가기
          </a>
        </div>
      </div>
      <div className="exchanger-cover"></div>
      <div className="cat-is-watching-you"></div>
    </div>
  );
}

export default App;
