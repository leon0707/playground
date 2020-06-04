#!/usr/bin/env node

const cdk = require('@aws-cdk/core');
const { AwsCdkHellowordStack } = require('../lib/aws-cdk-helloword-stack');

const app = new cdk.App();
new AwsCdkHellowordStack(app, 'AwsCdkHellowordStack');
