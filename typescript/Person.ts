// https://www.typescriptlang.org/docs/handbook/classes.html

enum Gender {
    Male,
    Female
}

export class Person {
    public readonly firstName: string;
    public readonly lastName: string;
    private readonly gender: Gender;

    constructor(firstName: string, lastName: string, gender: Gender) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.gender = gender;
    }

    public fullName() {
        return `${this.firstName} ${this.lastName}`;
    }
}