
"use strict";

let AttitudeCommand = require('./AttitudeCommand.js');
let MotorStatus = require('./MotorStatus.js');
let MotorCommand = require('./MotorCommand.js');
let RawRC = require('./RawRC.js');
let RuddersCommand = require('./RuddersCommand.js');
let RawMagnetic = require('./RawMagnetic.js');
let PositionXYCommand = require('./PositionXYCommand.js');
let Compass = require('./Compass.js');
let VelocityZCommand = require('./VelocityZCommand.js');
let RC = require('./RC.js');
let Altitude = require('./Altitude.js');
let MotorPWM = require('./MotorPWM.js');
let ServoCommand = require('./ServoCommand.js');
let Altimeter = require('./Altimeter.js');
let RawImu = require('./RawImu.js');
let ThrustCommand = require('./ThrustCommand.js');
let VelocityXYCommand = require('./VelocityXYCommand.js');
let YawrateCommand = require('./YawrateCommand.js');
let HeightCommand = require('./HeightCommand.js');
let Supply = require('./Supply.js');
let ControllerState = require('./ControllerState.js');
let HeadingCommand = require('./HeadingCommand.js');

module.exports = {
  AttitudeCommand: AttitudeCommand,
  MotorStatus: MotorStatus,
  MotorCommand: MotorCommand,
  RawRC: RawRC,
  RuddersCommand: RuddersCommand,
  RawMagnetic: RawMagnetic,
  PositionXYCommand: PositionXYCommand,
  Compass: Compass,
  VelocityZCommand: VelocityZCommand,
  RC: RC,
  Altitude: Altitude,
  MotorPWM: MotorPWM,
  ServoCommand: ServoCommand,
  Altimeter: Altimeter,
  RawImu: RawImu,
  ThrustCommand: ThrustCommand,
  VelocityXYCommand: VelocityXYCommand,
  YawrateCommand: YawrateCommand,
  HeightCommand: HeightCommand,
  Supply: Supply,
  ControllerState: ControllerState,
  HeadingCommand: HeadingCommand,
};
