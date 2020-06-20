import React from 'react';

import UseStateDemo from './UseStateDemo';
import UseEffectDemo from './UseEffectDemo';

import './ReactBasic.css';

function ReactBasic() {
  return (
    <div className="App">
      <div className="App-header">
        <h1>
          Demos
        </h1>
        <div>
          <h3>useState examples</h3>
          <UseStateDemo />
        </div>
        <div>
          <h3>useEffect examples</h3>
          <UseEffectDemo />
        </div>
      </div>
    </div>
  );
}

export default ReactBasic;
