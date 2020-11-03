# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ardrone_autonomy/navdata_kalman_pressure.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class navdata_kalman_pressure(genpy.Message):
  _md5sum = "70734b6caff0fb7ea6fc88ffeea5cde5"
  _type = "ardrone_autonomy/navdata_kalman_pressure"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
float64 drone_time
uint16 tag
uint16 size
float32 offset_pressure
float32 est_z
float32 est_zdot
float32 est_bias_PWM
float32 est_biais_pression
float32 offset_US
float32 prediction_US
float32 cov_alt
float32 cov_PWM
float32 cov_vitesse
int32 bool_effet_sol
float32 somme_inno
int32 flag_rejet_US
float32 u_multisinus
float32 gaz_altitude
int32 Flag_multisinus
int32 Flag_multisinus_debut

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
"""
  __slots__ = ['header','drone_time','tag','size','offset_pressure','est_z','est_zdot','est_bias_PWM','est_biais_pression','offset_US','prediction_US','cov_alt','cov_PWM','cov_vitesse','bool_effet_sol','somme_inno','flag_rejet_US','u_multisinus','gaz_altitude','Flag_multisinus','Flag_multisinus_debut']
  _slot_types = ['std_msgs/Header','float64','uint16','uint16','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','int32','float32','int32','float32','float32','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,drone_time,tag,size,offset_pressure,est_z,est_zdot,est_bias_PWM,est_biais_pression,offset_US,prediction_US,cov_alt,cov_PWM,cov_vitesse,bool_effet_sol,somme_inno,flag_rejet_US,u_multisinus,gaz_altitude,Flag_multisinus,Flag_multisinus_debut

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(navdata_kalman_pressure, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.drone_time is None:
        self.drone_time = 0.
      if self.tag is None:
        self.tag = 0
      if self.size is None:
        self.size = 0
      if self.offset_pressure is None:
        self.offset_pressure = 0.
      if self.est_z is None:
        self.est_z = 0.
      if self.est_zdot is None:
        self.est_zdot = 0.
      if self.est_bias_PWM is None:
        self.est_bias_PWM = 0.
      if self.est_biais_pression is None:
        self.est_biais_pression = 0.
      if self.offset_US is None:
        self.offset_US = 0.
      if self.prediction_US is None:
        self.prediction_US = 0.
      if self.cov_alt is None:
        self.cov_alt = 0.
      if self.cov_PWM is None:
        self.cov_PWM = 0.
      if self.cov_vitesse is None:
        self.cov_vitesse = 0.
      if self.bool_effet_sol is None:
        self.bool_effet_sol = 0
      if self.somme_inno is None:
        self.somme_inno = 0.
      if self.flag_rejet_US is None:
        self.flag_rejet_US = 0
      if self.u_multisinus is None:
        self.u_multisinus = 0.
      if self.gaz_altitude is None:
        self.gaz_altitude = 0.
      if self.Flag_multisinus is None:
        self.Flag_multisinus = 0
      if self.Flag_multisinus_debut is None:
        self.Flag_multisinus_debut = 0
    else:
      self.header = std_msgs.msg.Header()
      self.drone_time = 0.
      self.tag = 0
      self.size = 0
      self.offset_pressure = 0.
      self.est_z = 0.
      self.est_zdot = 0.
      self.est_bias_PWM = 0.
      self.est_biais_pression = 0.
      self.offset_US = 0.
      self.prediction_US = 0.
      self.cov_alt = 0.
      self.cov_PWM = 0.
      self.cov_vitesse = 0.
      self.bool_effet_sol = 0
      self.somme_inno = 0.
      self.flag_rejet_US = 0
      self.u_multisinus = 0.
      self.gaz_altitude = 0.
      self.Flag_multisinus = 0
      self.Flag_multisinus_debut = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_d2H10fifi2f2i().pack(_x.drone_time, _x.tag, _x.size, _x.offset_pressure, _x.est_z, _x.est_zdot, _x.est_bias_PWM, _x.est_biais_pression, _x.offset_US, _x.prediction_US, _x.cov_alt, _x.cov_PWM, _x.cov_vitesse, _x.bool_effet_sol, _x.somme_inno, _x.flag_rejet_US, _x.u_multisinus, _x.gaz_altitude, _x.Flag_multisinus, _x.Flag_multisinus_debut))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 80
      (_x.drone_time, _x.tag, _x.size, _x.offset_pressure, _x.est_z, _x.est_zdot, _x.est_bias_PWM, _x.est_biais_pression, _x.offset_US, _x.prediction_US, _x.cov_alt, _x.cov_PWM, _x.cov_vitesse, _x.bool_effet_sol, _x.somme_inno, _x.flag_rejet_US, _x.u_multisinus, _x.gaz_altitude, _x.Flag_multisinus, _x.Flag_multisinus_debut,) = _get_struct_d2H10fifi2f2i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_d2H10fifi2f2i().pack(_x.drone_time, _x.tag, _x.size, _x.offset_pressure, _x.est_z, _x.est_zdot, _x.est_bias_PWM, _x.est_biais_pression, _x.offset_US, _x.prediction_US, _x.cov_alt, _x.cov_PWM, _x.cov_vitesse, _x.bool_effet_sol, _x.somme_inno, _x.flag_rejet_US, _x.u_multisinus, _x.gaz_altitude, _x.Flag_multisinus, _x.Flag_multisinus_debut))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 80
      (_x.drone_time, _x.tag, _x.size, _x.offset_pressure, _x.est_z, _x.est_zdot, _x.est_bias_PWM, _x.est_biais_pression, _x.offset_US, _x.prediction_US, _x.cov_alt, _x.cov_PWM, _x.cov_vitesse, _x.bool_effet_sol, _x.somme_inno, _x.flag_rejet_US, _x.u_multisinus, _x.gaz_altitude, _x.Flag_multisinus, _x.Flag_multisinus_debut,) = _get_struct_d2H10fifi2f2i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_d2H10fifi2f2i = None
def _get_struct_d2H10fifi2f2i():
    global _struct_d2H10fifi2f2i
    if _struct_d2H10fifi2f2i is None:
        _struct_d2H10fifi2f2i = struct.Struct("<d2H10fifi2f2i")
    return _struct_d2H10fifi2f2i
