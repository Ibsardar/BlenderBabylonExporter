import bpy
import io
import json


def write_obj():
    
    listOfObjects = bpy.data.objects
    out2 = io.open('blenderLogic.json', 'w', encoding='utf8')
    sensorType = ''
    test = {'Objects' : []}
    for i in range(0, len(listOfObjects)):
        tempObject = {}
        tempObject['name'] = bpy.data.objects[i].name
        tempObject['type'] = bpy.data.objects[i].type
       
         #select the current object and take the mesh data from that
        bpy.context.scene.objects.active = bpy.data.objects[bpy.data.objects[i].name]      
        obj = bpy.context.active_object
      
        tempObject['shape'] = obj.data.name
        tempObject['physics'] = bpy.data.objects[i].game.physics_type 
        tempObject['mass'] = bpy.data.objects[i].game.mass
		
		
        
        tempObject['sensors'] = []
        tempObject['properties'] = []
        if tempObject['type'] == "CAMERA":
            tempVector = []
            tempVector.append(bpy.data.objects[i].rotation_euler[0])
            tempVector.append(bpy.data.objects[i].rotation_euler[1])
            tempVector.append(bpy.data.objects[i].rotation_euler[2])
            tempObject['rotation'] = tempVector
        test['Objects'].append(tempObject)
        for j in range(0, len(bpy.data.objects[i].game.properties)):
            prop = {}
            prop['name'] = bpy.data.objects[i].game.properties[j].name
            prop['value'] = bpy.data.objects[i].game.properties[j].value
            tempObject['properties'].append(prop)
        for j in range(0, len(bpy.data.objects[i].game.sensors)):
            #create Json object for all sensors
            tempSensor = {}
            tempSensor['name'] = bpy.data.objects[i].game.sensors[j].name
            print(bpy.data.objects[i].game.sensors[j].type)
            tempSensor['type'] = bpy.data.objects[i].game.sensors[j].type
            tempSensor['active'] = bpy.data.objects[i].game.sensors[j].active
            tempSensor['invert'] = bpy.data.objects[i].game.sensors[j].invert
            tempSensor['tap'] = bpy.data.objects[i].game.sensors[j].use_tap
            tempSensor['controllers'] = []
            
            if tempSensor['type'] == "KEYBOARD":
                tempSensor['key'] = bpy.data.objects[i].game.sensors[j].key
                tempSensor['allKeys'] = bpy.data.objects[i].game.sensors[j].use_all_keys
            
            elif tempSensor['type'] == "MESSAGE":
                tempSensor['subject'] = bpy.data.objects[i].game.sensors[j].subject
                    
            elif tempSensor['type'] == "COLLISION":
                tempSensor['material'] = bpy.data.objects[i].game.sensors[j].material
                tempSensor['property'] = bpy.data.objects[i].game.sensors[j].property
                tempSensor['useMaterial'] = bpy.data.objects[i].game.sensors[j].use_material
                
            elif tempSensor['type'] == "MOUSE":
                tempSensor['mouseEvent'] = bpy.data.objects[i].game.sensors[j].mouse_event
                tempSensor['useTap'] = bpy.data.objects[i].game.sensors[j].use_tap
                tempSensor['useXRay'] = bpy.data.objects[i].game.sensors[j].use_x_ray
                
            elif tempSensor['type'] == "RAY":
                tempSensor['axis'] = bpy.data.objects[i].game.sensors[j].axis
                tempSensor['material'] = bpy.data.objects[i].game.sensors[j].material
                tempSensor['property'] = bpy.data.objects[i].game.sensors[j].property
                tempSensor['range'] = bpy.data.objects[i].game.sensors[j].range
                tempSensor['rayType'] = bpy.data.objects[i].game.sensors[j].ray_type
                tempSensor['useXRay'] = bpy.data.objects[i].game.sensors[j].use_x_ray
                
            elif tempSensor['type'] == "JOYSTICK":
                tempSensor['axisDirection'] = bpy.data.objects[i].game.sensors[j].axis_direction
                tempSensor['axisNumber'] = bpy.data.objects[i].game.sensors[j].axis_number
                tempSensor['buttonNumber'] = bpy.data.objects[i].game.sensors[j].button_number
                tempSensor['eventType'] = bpy.data.objects[i].game.sensors[j].event_type
                tempSensor['hatDirection'] = bpy.data.objects[i].game.sensors[j].hat_direction
                tempSensor['hatNumber'] = bpy.data.objects[i].game.sensors[j].hat_number
                tempSensor['joystickIndex'] = bpy.data.objects[i].game.sensors[j].joystick_index
                tempSensor['single_axis_number'] = bpy.data.objects[i].game.sensors[j].single_axis_number
                tempSensor['useAllEvents'] = bpy.data.objects[i].game.sensors[j].use_all_events
            else:
                print()
                
            test['Objects'][i]["sensors"].append(tempSensor)
                
            for k in range(0,len(bpy.data.objects[i].game.sensors[j].controllers)):
                tempController = {} 
                tempController['name'] = bpy.data.objects[i].game.sensors[j].controllers[k].name
                tempController['type'] = bpy.data.objects[i].game.sensors[j].controllers[k].type
                tempController['active'] = bpy.data.objects[i].game.sensors[j].controllers[k].active
                tempController['actuators'] = []
                test['Objects'][i]["sensors"][j]['controllers'].append(tempController)

                for l in range(0, len(bpy.data.objects[i].game.sensors[j].controllers[k].actuators)):
                    tempActuator = {} 
                    tempActuator['name'] = bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].name
                    tempActuator['type'] = bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].type
                    tempActuator['active'] = bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].active
                    if tempActuator['type'] == "MOTION":
                        tempActuator['localLocation'] = bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].use_local_location
                        tempActuator['localRotation'] = bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].use_local_rotation
                        #convert Vector to an array
                        tempVector = [bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].offset_location.x,bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].offset_location.y, bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].offset_location.z ] 
                        tempActuator['offsetLocation'] = tempVector
                        tempVector2 = [bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].offset_rotation.x,bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].offset_rotation.y, bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].offset_rotation.z]
                        tempActuator['offsetRotation'] = tempVector2
                        tempVector = [bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].offset_location.x,bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].offset_location.y, bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].offset_location.z ] 
                        tempActuator['offsetLocation'] = tempVector
                        tempVector2 = [bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].offset_rotation.x,bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].offset_rotation.y, bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].offset_rotation.z]
                        tempActuator['offsetRotation'] = tempVector2
                        tempVector3 = [bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].force.x,bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].force.y, bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].force.z]
                        tempActuator['force'] = tempVector3
                        tempVector4 = [bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].linear_velocity.x, bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].linear_velocity.y, bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].linear_velocity.z]
                        tempActuator['linearVelocity'] = tempVector4
                        tempVector5 = [bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].angular_velocity.x, bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].angular_velocity.y, bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].angular_velocity.z]
                        tempActuator['angularVelocity'] = tempVector5

                    elif tempActuator['type'] == "VISIBILITY":
                        tempActuator['visible'] = bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].use_visible
                    
                    elif tempActuator['type'] == "PARENT":
                        tempActuator['toBeParent'] = bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].object.name
                    
                    elif tempActuator['type'] == "MESSAGE":
                        tempActuator['to'] = bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].to_property
                        tempActuator['subject'] = bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].subject
                        tempActuator['message'] = bpy.data.objects[i].game.sensors[j].controllers[k].actuators[l].body_message
                        
                    test['Objects'][i]["sensors"][j]['controllers'][k]['actuators'].append(tempActuator)
    
    print(test)
    print(json.dumps(test, default=lambda o: o.dict))
    out2.write(json.dumps(test, default=lambda o: o.dict))
    out2.close()
        
write_obj()