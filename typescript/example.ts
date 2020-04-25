import INums from './numInterface';

enum Direction {
    Up = "UP",
    Down = "DOWN",
    Left = "LEFT",
    Right = "RIGHT",
}

const nums: ( number | boolean )[] = [1,2,3,4,5,true];

const nums_1: any[] = [1,2,3,4,5,true];

function add(n1: number, n2: number): number {



    return n1 + n2;
}

type numType = {
    num1: number,
    num2: number
}

function addNum(nums: numType): number {
    return nums.num1 + nums.num2;
}

addNum({num1: 1, num2: 2})