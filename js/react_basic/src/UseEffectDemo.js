import React, { useState, useEffect } from 'react';

function Clock(props) {
  const [time, setTime] = useState(new Date());
  let timeInterval;
  useEffect(() => {
    timeInterval = setInterval(() => {
      setTime(new Date());
    }, 1000);
    return function cleanup() {
      //clean interval when component unmounts
      clearInterval(timeInterval);
    };
  },
  // no depency so callback only run once when component renders first time.
  []);

  return (
    <p>{time.toString()}</p>
  );
}

function Subscriber(props) {
  const [isSubscribe, setIsSubscribe] = useState(false);
  useEffect((p) => {
    // callback runs every time isSubscribe is changed, isSubscribe is the new value for this render
    console.log('useEffect', isSubscribe)
    if(isSubscribe) {
      props.subscribe(true);
    }
    return function cleanup(p) {
      console.log('cleanup', isSubscribe);
      // runs every time isSubscribe is changed. isSubscribe in this function is a copy of last render
      props.subscribe(false);
    };
  }, [isSubscribe]);
  return (
    <>
      <p>{`Subscriber ${isSubscribe ? '' : 'not '}subscribe`}</p>
      <button onClick={(e) => setIsSubscribe(!isSubscribe)}>
        toggle subscribe
      </button>
    </>
  );
}

function UseEffectDemo(props) {
  const colors = ['white', 'red', 'blue', 'green', 'azure', 'cyan', 'ivory'];
  const [colorNum, setColorNum] = useState(0);
  const [noDep, setNoDep] = useState(1);
  const [showClock, setShowClock] = useState(true);

  const onClickHandler = (change) => {
    return (e) => {
      let _colorNum = (colorNum + change) % colors.length === - 1 ? colors.length - 1 : (colorNum + change) % colors.length;
      setColorNum(_colorNum);
    }
  }

  useEffect(() => {
    // update dom after render
    document.body.style.backgroundColor = colors[colorNum * noDep];
  },
  // noDep is not a dependency, so it won't trigger the call back func
  [colorNum]);

  const [isSubscribed, setIsSubscribed] = useState(false);
  const subscribe = (_isSubscribed) => {
    // console.log(_isSubscribed);
    setIsSubscribed(_isSubscribed);
  }

  return (
    <>
      <div>
        <p>Color: { colors[colorNum] }</p>
        <button onClick={onClickHandler(-1)}>
          prev
        </button>
        <button onClick={onClickHandler(1)}>
          next
        </button>
        <button onClick={(e) => setNoDep(0)}>
          {noDep} white not working
        </button>
      </div>
      <div>
        {showClock &&
          <Clock />
        }
        <button onClick={(e) => setShowClock(!showClock)}>
          toggle clock
        </button>
      </div>
      <div>
        <Subscriber subscribe={subscribe} />
        <p>{`${isSubscribed ? '' : 'not '} subscribed`}</p>
      </div>
    </>
  );
}

export default UseEffectDemo;