#!/usr/bin/env python
# -*- coding:utf-8 -*-


# ############################################################################
#  license :
# ============================================================================
#
#  File :        Relay.py
#
#  Project :     
#
# This file is part of Tango device class.
# 
# Tango is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Tango is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Tango.  If not, see <http://www.gnu.org/licenses/>.
# 
#
#  $Author :      maxim.stassevich$
#
#  $Revision :    $
#
#  $Date :        $
#
#  $HeadUrl :     $
# ============================================================================
#            This file is generated by POGO
#     (Program Obviously used to Generate tango Object)
# ############################################################################

__all__ = ["Relay", "RelayClass", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
# Add additional import
#----- PROTECTED REGION ID(Relay.additionnal_import) ENABLED START -----#
import smbus


class Relay1():
    def __init__(self):
        self.DEVICE_ADDRESS = 0x20  # 7 bit address (will be left shifted to add the read write bit)
        self.DEVICE_REG_MODE1 = 0x06
        self.DEVICE_REG_DATA = 0xff
        self.bus = smbus.SMBus(1)  # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
        self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)
    
    def ON_1(self):
        #print('ON_1...')
        self.DEVICE_REG_DATA &= ~(0x1 << 0)
        self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def ON_2(self):
        #print('ON_2...')
        self.DEVICE_REG_DATA &= ~(0x1 << 1)
        self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def ON_3(self):
        #print('ON_3...')
        self.DEVICE_REG_DATA &= ~(0x1 << 2)
        self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def ON_4(self):
        #print('ON_4...')
        self.DEVICE_REG_DATA &= ~(0x1 << 3)
        self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def OFF_1(self):
        #print('OFF_1...')
        self.DEVICE_REG_DATA |= (0x1 << 0)
        self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def OFF_2(self):
        #print('OFF_2...')
        self.DEVICE_REG_DATA |= (0x1 << 1)
        self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def OFF_3(self):
        #print('OFF_3...')
        self.DEVICE_REG_DATA |= (0x1 << 2)
        self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def OFF_4(self):
        #print('OFF_4...')
        self.DEVICE_REG_DATA |= (0x1 << 3)
        self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def ALLON(self):
        #print('ALL ON...')
        self.DEVICE_REG_DATA &= ~(0xf << 0)
        self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def ALLOFF(self):
        #print('ALL OFF...')
        self.DEVICE_REG_DATA |= (0xf << 0)
        self.bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)




#----- PROTECTED REGION END -----#	//	Relay.additionnal_import

# Device States Description
# ON : 
# OFF : 


class Relay (PyTango.Device_4Impl):
    """Class to control relay with raspberry"""
    
    # -------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(Relay.global_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	Relay.global_variables

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        Relay.init_device(self)
        #----- PROTECTED REGION ID(Relay.__init__) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Relay.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(Relay.delete_device) ENABLED START -----#
        try:
            self.relay.ALLOFF()
        except:
            pass
        if self.get_state() != PyTango.DevState.OFF:
            self.set_state(PyTango.DevState.OFF)
            self.set_status("Device is in OFF state")
        #----- PROTECTED REGION END -----#	//	Relay.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        self.attr_relay1_read = False
        self.attr_relay2_read = False
        self.attr_relay3_read = False
        self.attr_relay4_read = False
        #----- PROTECTED REGION ID(Relay.init_device) ENABLED START -----#
        try:
            if self.get_state() != PyTango.DevState.ON:
                self.set_state(PyTango.DevState.ON)
                self.set_status("Device is in ON state")
            self.relay = Relay1()
            self.relay.ALLOFF()
        except:
            if self.get_state() != PyTango.DevState.OFF:
                self.set_state(PyTango.DevState.OFF)
                self.set_status("Device is in OFF state")
        
        #----- PROTECTED REGION END -----#	//	Relay.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(Relay.always_executed_hook) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Relay.always_executed_hook

    # -------------------------------------------------------------------------
    #    Relay read/write attribute methods
    # -------------------------------------------------------------------------
    
    def read_relay1(self, attr):
        self.debug_stream("In read_relay1()")
        #----- PROTECTED REGION ID(Relay.relay1_read) ENABLED START -----#
        attr.set_value(self.attr_relay1_read)
        
        #----- PROTECTED REGION END -----#	//	Relay.relay1_read
        
    def write_relay1(self, attr):
        self.debug_stream("In write_relay1()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(Relay.relay1_write) ENABLED START -----#
        try:
            if self.get_state() != PyTango.DevState.ON:
                self.set_state(PyTango.DevState.ON)
                self.set_status("Device is in ON state")
            if data == False:
                self.relay.OFF_1()
                self.attr_relay1_read = False
            else:
                self.relay.ON_1()
                self.attr_relay1_read = True
        except:
            if self.get_state() != PyTango.DevState.OFF:
                self.set_state(PyTango.DevState.OFF)
                self.set_status("Device is in OFF state")
        #----- PROTECTED REGION END -----#	//	Relay.relay1_write
        
    def is_relay1_allowed(self, attr):
        self.debug_stream("In is_relay1_allowed()")
        if attr==PyTango.AttReqType.READ_REQ:
            state_ok = not(self.get_state() in [PyTango.DevState.OFF])
        else:
            state_ok = not(self.get_state() in [PyTango.DevState.OFF])
        #----- PROTECTED REGION ID(Relay.is_relay1_allowed) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Relay.is_relay1_allowed
        return state_ok
        
    def read_relay2(self, attr):
        self.debug_stream("In read_relay2()")
        #----- PROTECTED REGION ID(Relay.relay2_read) ENABLED START -----#
        attr.set_value(self.attr_relay2_read)
        
        #----- PROTECTED REGION END -----#	//	Relay.relay2_read
        
    def write_relay2(self, attr):
        self.debug_stream("In write_relay2()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(Relay.relay2_write) ENABLED START -----#
        try:
            if self.get_state() != PyTango.DevState.ON:
                self.set_state(PyTango.DevState.ON)
                self.set_status("Device is in ON state")
            if data == False:
                self.relay.OFF_2()
                self.attr_relay2_read = False
            else:
                self.relay.ON_2()
                self.attr_relay2_read = True
        except:
            if self.get_state() != PyTango.DevState.OFF:
                self.set_state(PyTango.DevState.OFF)
                self.set_status("Device is in OFF state")
        #----- PROTECTED REGION END -----#	//	Relay.relay2_write
        
    def is_relay2_allowed(self, attr):
        self.debug_stream("In is_relay2_allowed()")
        if attr==PyTango.AttReqType.READ_REQ:
            state_ok = not(self.get_state() in [PyTango.DevState.OFF])
        else:
            state_ok = not(self.get_state() in [PyTango.DevState.OFF])
        #----- PROTECTED REGION ID(Relay.is_relay2_allowed) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Relay.is_relay2_allowed
        return state_ok
        
    def read_relay3(self, attr):
        self.debug_stream("In read_relay3()")
        #----- PROTECTED REGION ID(Relay.relay3_read) ENABLED START -----#
        attr.set_value(self.attr_relay3_read)
        
        #----- PROTECTED REGION END -----#	//	Relay.relay3_read
        
    def write_relay3(self, attr):
        self.debug_stream("In write_relay3()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(Relay.relay3_write) ENABLED START -----#
        try:
            if self.get_state() != PyTango.DevState.ON:
                self.set_state(PyTango.DevState.ON)
                self.set_status("Device is in ON state")
            if data == False:
                self.relay.OFF_3()
                self.attr_relay3_read = False
            else:
                self.relay.ON_3()
                self.attr_relay3_read = True
        except:
            if self.get_state() != PyTango.DevState.OFF:
                self.set_state(PyTango.DevState.OFF)
                self.set_status("Device is in OFF state")
        #----- PROTECTED REGION END -----#	//	Relay.relay3_write
        
    def is_relay3_allowed(self, attr):
        self.debug_stream("In is_relay3_allowed()")
        if attr==PyTango.AttReqType.READ_REQ:
            state_ok = not(self.get_state() in [PyTango.DevState.OFF])
        else:
            state_ok = not(self.get_state() in [PyTango.DevState.OFF])
        #----- PROTECTED REGION ID(Relay.is_relay3_allowed) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Relay.is_relay3_allowed
        return state_ok
        
    def read_relay4(self, attr):
        self.debug_stream("In read_relay4()")
        #----- PROTECTED REGION ID(Relay.relay4_read) ENABLED START -----#
        attr.set_value(self.attr_relay4_read)
        
        #----- PROTECTED REGION END -----#	//	Relay.relay4_read
        
    def write_relay4(self, attr):
        self.debug_stream("In write_relay4()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(Relay.relay4_write) ENABLED START -----#
        try:
            if self.get_state() != PyTango.DevState.ON:
                self.set_state(PyTango.DevState.ON)
                self.set_status("Device is in ON state")
            if data == False:
                self.relay.OFF_4()
                self.attr_relay4_read = False
            else:
                self.relay.ON_4()
                self.attr_relay4_read = True
        except:
            if self.get_state() != PyTango.DevState.OFF:
                self.set_state(PyTango.DevState.OFF)
                self.set_status("Device is in OFF state")
        #----- PROTECTED REGION END -----#	//	Relay.relay4_write
        
    def is_relay4_allowed(self, attr):
        self.debug_stream("In is_relay4_allowed()")
        if attr==PyTango.AttReqType.READ_REQ:
            state_ok = not(self.get_state() in [PyTango.DevState.OFF])
        else:
            state_ok = not(self.get_state() in [PyTango.DevState.OFF])
        #----- PROTECTED REGION ID(Relay.is_relay4_allowed) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Relay.is_relay4_allowed
        return state_ok
        
    
    
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(Relay.read_attr_hardware) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Relay.read_attr_hardware


    # -------------------------------------------------------------------------
    #    Relay command methods
    # -------------------------------------------------------------------------
    
    def all_on(self):
        """ All relays switch to on
        """
        self.debug_stream("In all_on()")
        #----- PROTECTED REGION ID(Relay.all_on) ENABLED START -----#
        try:
            if self.get_state() != PyTango.DevState.ON:
                self.set_state(PyTango.DevState.ON)
                self.set_status("Device is in ON state")
            self.relay.ALLON()
            self.attr_relay1_read = True
            self.attr_relay2_read = True
            self.attr_relay3_read = True
            self.attr_relay4_read = True
        except:
            if self.get_state() != PyTango.DevState.OFF:
                self.set_state(PyTango.DevState.OFF)
                self.set_status("Device is in OFF state")
        #----- PROTECTED REGION END -----#	//	Relay.all_on
        
    def is_all_on_allowed(self):
        self.debug_stream("In is_all_on_allowed()")
        state_ok = not(self.get_state() in [PyTango.DevState.OFF])
        #----- PROTECTED REGION ID(Relay.is_all_on_allowed) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Relay.is_all_on_allowed
        return state_ok
        
    def all_off(self):
        """ All relays switch to off
        """
        self.debug_stream("In all_off()")
        #----- PROTECTED REGION ID(Relay.all_off) ENABLED START -----#
        try:
            if self.get_state() != PyTango.DevState.ON:
                self.set_state(PyTango.DevState.ON)
                self.set_status("Device is in ON state")
            self.relay.ALLOFF()
            self.attr_relay1_read = False
            self.attr_relay2_read = False
            self.attr_relay3_read = False
            self.attr_relay4_read = False
        except:
            if self.get_state() != PyTango.DevState.OFF:
                self.set_state(PyTango.DevState.OFF)
                self.set_status("Device is in OFF state")
        #----- PROTECTED REGION END -----#	//	Relay.all_off
        
    def is_all_off_allowed(self):
        self.debug_stream("In is_all_off_allowed()")
        state_ok = not(self.get_state() in [PyTango.DevState.OFF])
        #----- PROTECTED REGION ID(Relay.is_all_off_allowed) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Relay.is_all_off_allowed
        return state_ok
        

    #----- PROTECTED REGION ID(Relay.programmer_methods) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	Relay.programmer_methods

class RelayClass(PyTango.DeviceClass):
    # -------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(Relay.global_class_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	Relay.global_class_variables


    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
        }


    #    Command definitions
    cmd_list = {
        'all_on':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        'all_off':
            [[PyTango.DevVoid, "none"],
            [PyTango.DevVoid, "none"]],
        }


    #    Attribute definitions
    attr_list = {
        'relay1':
            [[PyTango.DevBoolean,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'label': "relay1",
            } ],
        'relay2':
            [[PyTango.DevBoolean,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'label': "relay2",
            } ],
        'relay3':
            [[PyTango.DevBoolean,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'label': "relay3",
            } ],
        'relay4':
            [[PyTango.DevBoolean,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'label': "relay4",
            } ],
        }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(RelayClass, Relay, 'Relay')
        #----- PROTECTED REGION ID(Relay.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Relay.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

if __name__ == '__main__':
    main()
