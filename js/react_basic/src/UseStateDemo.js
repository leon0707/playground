import React, { useState } from 'react';

function UseStateDemo(props) {
  const [count, setCount] = useState(0);
  const onClickHandler = (change) => {
    return (e) => {
      setCount(count + change)
    }
  }

  const [name, setName] = useState({
    firstName: '',
    lastName: ''
  });

  const onChangeHandler = (attr) => {
    return (e) => {
      // must copy the value to avoid the setState pitfall
      let currentVal = e.target.value;
      setName(preName => {
        return {
          ...preName,
          [attr]: currentVal
        }
      });
    }
  }

  return (
    <>
      <div>
        <p>Counter: { count }</p>
        <button onClick={onClickHandler(1)}>
          + 1
        </button>
        <button onClick={onClickHandler(-1)}>
          - 1
        </button>
      </div>
      <div>
        <p>Name: {`${name.firstName} ${name.lastName}`}</p>
        <input placeholder="first name" onChange={onChangeHandler('firstName')} value={name.firstName} />
        <input placeholder="last name" onChange={onChangeHandler('lastName')} value={name.lastName}/>
      </div>
    </>
  );
}

export default UseStateDemo;