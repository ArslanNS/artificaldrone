
"use strict";

let MotorStatus = require('./MotorStatus.js');
let AttitudeCommand = require('./AttitudeCommand.js');
let ControllerState = require('./ControllerState.js');
let Altimeter = require('./Altimeter.js');
let RawImu = require('./RawImu.js');
let PositionXYCommand = require('./PositionXYCommand.js');
let YawrateCommand = require('./YawrateCommand.js');
let RuddersCommand = require('./RuddersCommand.js');
let HeightCommand = require('./HeightCommand.js');
let HeadingCommand = require('./HeadingCommand.js');
let RawMagnetic = require('./RawMagnetic.js');
let ThrustCommand = require('./ThrustCommand.js');
let ServoCommand = require('./ServoCommand.js');
let RawRC = require('./RawRC.js');
let MotorCommand = require('./MotorCommand.js');
let VelocityXYCommand = require('./VelocityXYCommand.js');
let Compass = require('./Compass.js');
let MotorPWM = require('./MotorPWM.js');
let Supply = require('./Supply.js');
let RC = require('./RC.js');
let VelocityZCommand = require('./VelocityZCommand.js');
let LandingActionFeedback = require('./LandingActionFeedback.js');
let PoseGoal = require('./PoseGoal.js');
let PoseActionGoal = require('./PoseActionGoal.js');
let PoseActionResult = require('./PoseActionResult.js');
let PoseFeedback = require('./PoseFeedback.js');
let PoseAction = require('./PoseAction.js');
let LandingFeedback = require('./LandingFeedback.js');
let TakeoffActionFeedback = require('./TakeoffActionFeedback.js');
let LandingAction = require('./LandingAction.js');
let TakeoffResult = require('./TakeoffResult.js');
let LandingGoal = require('./LandingGoal.js');
let TakeoffFeedback = require('./TakeoffFeedback.js');
let TakeoffActionGoal = require('./TakeoffActionGoal.js');
let PoseActionFeedback = require('./PoseActionFeedback.js');
let LandingActionGoal = require('./LandingActionGoal.js');
let TakeoffGoal = require('./TakeoffGoal.js');
let LandingActionResult = require('./LandingActionResult.js');
let TakeoffActionResult = require('./TakeoffActionResult.js');
let LandingResult = require('./LandingResult.js');
let PoseResult = require('./PoseResult.js');
let TakeoffAction = require('./TakeoffAction.js');

module.exports = {
  MotorStatus: MotorStatus,
  AttitudeCommand: AttitudeCommand,
  ControllerState: ControllerState,
  Altimeter: Altimeter,
  RawImu: RawImu,
  PositionXYCommand: PositionXYCommand,
  YawrateCommand: YawrateCommand,
  RuddersCommand: RuddersCommand,
  HeightCommand: HeightCommand,
  HeadingCommand: HeadingCommand,
  RawMagnetic: RawMagnetic,
  ThrustCommand: ThrustCommand,
  ServoCommand: ServoCommand,
  RawRC: RawRC,
  MotorCommand: MotorCommand,
  VelocityXYCommand: VelocityXYCommand,
  Compass: Compass,
  MotorPWM: MotorPWM,
  Supply: Supply,
  RC: RC,
  VelocityZCommand: VelocityZCommand,
  LandingActionFeedback: LandingActionFeedback,
  PoseGoal: PoseGoal,
  PoseActionGoal: PoseActionGoal,
  PoseActionResult: PoseActionResult,
  PoseFeedback: PoseFeedback,
  PoseAction: PoseAction,
  LandingFeedback: LandingFeedback,
  TakeoffActionFeedback: TakeoffActionFeedback,
  LandingAction: LandingAction,
  TakeoffResult: TakeoffResult,
  LandingGoal: LandingGoal,
  TakeoffFeedback: TakeoffFeedback,
  TakeoffActionGoal: TakeoffActionGoal,
  PoseActionFeedback: PoseActionFeedback,
  LandingActionGoal: LandingActionGoal,
  TakeoffGoal: TakeoffGoal,
  LandingActionResult: LandingActionResult,
  TakeoffActionResult: TakeoffActionResult,
  LandingResult: LandingResult,
  PoseResult: PoseResult,
  TakeoffAction: TakeoffAction,
};
