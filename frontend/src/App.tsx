import React from "react";
import { Helmet } from "react-helmet";
import "./App.css";
import Dropdown from "./dropdown";

function App() {
  return (
    <div className="App">
      <Helmet htmlAttributes={{ lang: "kr" }}></Helmet>
      <div className="black-nav">
        <div className="nav-left">
          <span style={{ paddingRight: "15px" }}>이것저것 환율 계산기</span>
          <span>{DarkMode()}</span>
        </div>
        <div className="nav-right">
          <a {...to_sitecode}>코드 보러가기</a>
        </div>
      </div>
      <div className="exchanger-cover"></div>
      <div className="cat-is-watching-you"></div>
    </div>
  );
}

const to_sitecode = {
  href: "https://github.com/PzaThief/egg-exchanger",
  target: "_blank",
  style: { color: "inherit", textDecoration: "inherit" },
};

const DarkMode = () => {
  const body = document.documentElement;
  const lightTheme = "light";
  const darkTheme = "dark";
  let theme: any;

  if (localStorage) {
    theme = localStorage.getItem("theme");
  }

  if (theme === lightTheme || theme === darkTheme) {
    body.classList.add(theme);
  } else {
    body.classList.add(lightTheme);
  }

  const switchTheme = (e: any) => {
    if (theme === darkTheme) {
      body.classList.replace(darkTheme, lightTheme);
      localStorage.setItem("theme", "light");
      theme = lightTheme;
    } else {
      body.classList.replace(lightTheme, darkTheme);
      localStorage.setItem("theme", "dark");
      theme = darkTheme;
    }
    e.target.innerHTML = theme + " mode";
  };

  return (
    <button id="darkMode" onClick={(e) => switchTheme(e)}>
      {theme + " mode"}
    </button>
  );
};

export default App;
