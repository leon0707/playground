import React from 'react';

import UseStateDemo from './UseStateDemo';

import './ReactBasic.css';

function ReactBasic() {
  return (
    <div className="App">
      <div className="App-header">
        <h1>
          Demos
        </h1>
        <div>
          <h3>useSate examples</h3>
          <UseStateDemo />
        </div>
      </div>
    </div>
  );
}

export default ReactBasic;
