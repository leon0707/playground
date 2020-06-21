import React, { useState, useContext } from 'react';

import { ThemeContext, UserContext, themes } from './ThemeContext';

class Header extends React.Component {
  render() {
    let { theme } = this.context;
    return <h2 style={{ backgroundColor: theme.background, color: theme.foreground }}>this is a header</h2>
  }
}

// only support one context
Header.contextType = ThemeContext;

function Paragraph(props) {
  const { theme, toggleTheme } = useContext(ThemeContext);

  return (
    <>
      <p style={{ backgroundColor: theme.background, color: theme.foreground }}>this is a paragraph</p>
      <button onClick={(e) => toggleTheme()}>change theme</button>
    </>
  );
}

class Block extends React.Component {
  render() {
    return (
      <ThemeContext.Consumer>
      {({theme}) => (
        <UserContext.Consumer>
          {({id, name}) => (
            <>
              <p style={{ backgroundColor: theme.background, color: theme.foreground }}>{`ID: ${id} Name: ${name}`}</p>
            </>
          )}
        </UserContext.Consumer>
      )}
    </ThemeContext.Consumer>
    );
  }
}

function ContextDemo() {
  const [theme, setTheme] = useState(themes.light);

  const toggleTheme = () => {
    setTheme(theme === themes.dark ? themes.light: themes.dark);
  }
  
  return (
    <div>
      <ThemeContext.Provider value={{theme: themes.dark, toggleTheme: toggleTheme}}>
        <Header />
      </ThemeContext.Provider>
      <ThemeContext.Provider value={{theme: theme, toggleTheme: toggleTheme}}>
        <Paragraph />
      </ThemeContext.Provider>
      <ThemeContext.Provider value={{theme: theme, toggleTheme: toggleTheme}}>
        <UserContext.Provider value={{id: '123', name: 'Joe Doe'}}>
          <Block />
        </UserContext.Provider>
      </ThemeContext.Provider>
    </div>
  );
}

export default ContextDemo;