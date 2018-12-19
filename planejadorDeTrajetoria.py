if position_.x == desired_position_.x and position_.y == desired_position_.y:
        rospy.loginfo("Cheguei na posicao")

    if regions['front'] <= 14 and regions['front'] > 12:
      if position_.x - desired_position_.x >= 0.36 and position_.y - desired_position_.y >= 0.36 and position_.x - desired_position_.x < 0.64 and position_.y - desired_position_.y < 0.64:
        # vai mais devagar
      elif position_.x - desired_position_.x >= 0.64 and position_.y - desired_position_.y >= 0.64 and position_.x - desired_position_.x < 0.98 and position_.y - desired_position_.y < 0.98:
        # aumenta um pouco a velocidade
      elif position_.x - desired_position_.x >= 0.98 and position_.y - desired_position_.y >= 0.98 and position_.x - desired_position_.x < 1.50 and position_.y - desired_position_.y < 1.50:
        # velocidade normal
      else
        # soh anda normal

    elif regions['front'] <= 12 and regions['front'] > 8:
      if position_.x - desired_position_.x >= 0.36 and position_.y - desired_position_.y >= 0.36 and position_.x - desired_position_.x < 0.64 and position_.y - desired_position_.y < 0.64:
        # vai mais devagar
      elif position_.x - desired_position_.x >= 0.64 and position_.y - desired_position_.y >= 0.64 and position_.x - desired_position_.x < 0.98 and position_.y - desired_position_.y < 0.98:
        # aumenta um pouco a velocidade
      elif position_.x - desired_position_.x >= 0.98 and position_.y - desired_position_.y >= 0.98 and position_.x - desired_position_.x < 1.50 and position_.y - desired_position_.y < 1.50:
        # velocidade normal
      else
        # soh anda normal

    elif regions['front'] <= 12 and regions['front'] > 8:
      if position_.x - desired_position_.x >= 0.36 and position_.y - desired_position_.y >= 0.36 and position_.x - desired_position_.x < 0.64 and position_.y - desired_position_.y < 0.64:
        # vai mais devagar
      elif position_.x - desired_position_.x >= 0.64 and position_.y - desired_position_.y >= 0.64 and position_.x - desired_position_.x < 0.98 and position_.y - desired_position_.y < 0.98:
        # aumenta um pouco a velocidade
      elif position_.x - desired_position_.x >= 0.98 and position_.y - desired_position_.y >= 0.98 and position_.x - desired_position_.x < 1.50 and position_.y - desired_position_.y < 1.50:
        # velocidade normal
      else
        # soh anda normal

    elif regions['front'] <= 4.66 and regions['front'] >= 0.2037:
        if regions['front'] <= 4.66 and regions['front'] > 1.99 and position_.x - desired_position_.x >= -0.36 and position_.y - desired_position_.y >= -0.36 and position_.x - desired_position_.x < -0.04 and position_.y - desired_position_.y < -0.04:
            rospy.loginfo("Position: [%.2f, %.2f]",position_.x, position_.y)
            state_description = 'caso 1 - distanciaPequena'
            change_state(3)
        elif regions['front'] <= 4.66 and regions['front'] > 1.99 and position_.x - desired_position_.x >= -0.04 and position_.y - desired_position_.y >= -0.04 and position_.x - desired_position_.x < 0.0171 and position_.y - desired_position_.y < 0.0171:
            rospy.loginfo("Position: [%.2f, %.2f]",position_.x, position_.y)
            state_description = 'caso 1 - distanciaPequena'
            change_state(3)
        elif regions['front'] <= 4.66 and regions['front'] > 1.99 and position_.x - desired_position_.x >= 0.0171 and position_.y - desired_position_.y >= 0.0171 and position_.x - desired_position_.x < 0.263 and position_.y - desired_position_.y < 0.263:
            rospy.loginfo("Position: [%.2f, %.2f]",position_.x, position_.y)
            state_description = 'caso 1 - distanciaPequena'
            change_state(3)
        elif regions['front'] <= 1.99 and regions['front'] > 0.2037  and position_.x - desired_position_.x >= -0.04 and position_.y - desired_position_.y >= -0.04 and position_.x - desired_position_.x < 0.0171 and position_.y - desired_position_.y < 0.0171:
            rospy.loginfo("Position: [%.2f, %.2f]",position_.x, position_.y)
            state_description = 'caso 1 - distanciaPequena2'
            change_state(4)
        elif regions['front'] <= 1.99 and regions['front'] > 0.2037 and position_.x - desired_position_.x >= -0.36 and position_.y - desired_position_.y >= -0.36 and position_.x - desired_position_.x < -0.04 and position_.y - desired_position_.y < -0.04: 
            rospy.loginfo("Position: [%.2f, %.2f]",position_.x, position_.y)
            state_description = 'caso 1 - distanciaPequena2'
            change_state(4)
        elif regions['front'] <= 1.99 and regions['front'] > 0.2037 and position_.x - desired_position_.x >= 0.0171 and position_.y - desired_position_.y >= 0.0171 and position_.x - desired_position_.x < 0.263 and position_.y - desired_position_.y < 0.263: 
            rospy.loginfo("Position: [%.2f, %.2f]",position_.x, position_.y)
            state_description = 'caso 1 - distanciaPequena2'
            change_state(4)
        elif regions['front'] <= 0.2037 and regions['front'] > -1.08 and position_.x - desired_position_.x >= 0.0171 and position_.y - desired_position_.y >= 0.0171 and position_.x - desired_position_.x < 0.263 and position_.y - desired_position_.y < 0.263:
            rospy.loginfo("Position: [%.2f, %.2f]",position_.x, position_.y)
            state_description = 'caso 1 - distanciaPequena3'
            change_state(5)
        elif regions['front'] <= 0.2037 and regions['front'] > -1.08 and position_.x - desired_position_.x >= -0.04 and position_.y - desired_position_.y >= -0.04 and position_.x - desired_position_.x < 0.0171 and position_.y - desired_position_.y < 0.0171:
            rospy.loginfo("Position: [%.2f, %.2f]",position_.x, position_.y)
            state_description = 'caso 1 - distanciaPequena3'
            change_state(5)
        elif regions['front'] <= 0.2037 and regions['front'] > -1.08 and position_.x - desired_position_.x >= -0.36 and position_.y - desired_position_.y >= -0.36 and position_.x - desired_position_.x < -0.04 and position_.y - desired_position_.y < -0.04:
            rospy.loginfo("Position: [%.2f, %.2f]",position_.x, position_.y)
            state_description = 'caso 1 - distanciaPequena3'
            change_state(5)
    elif regions['front'] >= 6.002 and regions['front'] <= 11.192 and position_.x - desired_position_.x >= 0.152 and position_.y - desired_position_.y >= 0.152 and position_.x - desired_position_.x < 0.816 and position_.y - desired_position_.y < 0.816:
        rospy.loginfo("Position: [%.2f, %.2f]",position_.x, position_.y)
        state_description = 'caso 1 - distanciaMedia'
        change_state(6)
    
    elif regions['front'] >= 9.167 and regions['front'] <= 20.13:
        if regions['front'] >= 9.167 and regions['front'] < 13.137 and position_.x - desired_position_.x >= 0.697 and position_.y - desired_position_.y >= 0.697 and position_.x - desired_position_.x < 0.96 and position_.y - desired_position_.y < 0.96:
            rospy.loginfo("Position: [%.2f, %.2f]",position_.x, position_.y)
            state_description = 'caso 1 - distanciaGrande1'
            change_state(7)
        elif regions['front'] >= 9.167 and regions['front'] < 13.137 and position_.x - desired_position_.x >= 0.96 and position_.y - desired_position_.y >= 0.96 and position_.x - desired_position_.x < 1.04 and position_.y - desired_position_.y < 1.04:
            rospy.loginfo("Position: [%.2f, %.2f]",position_.x, position_.y)
            state_description = 'caso 1 - distanciaGrande1'
            change_state(7)
        elif regions['front'] >= 9.167 and regions['front'] < 13.137 and position_.x - desired_position_.x >= 1.04 and position_.y - desired_position_.y >= 1.04 and position_.x - desired_position_.x < 1.36 and position_.y - desired_position_.y < 1.36:
            rospy.loginfo("Position: [%.2f, %.2f]",position_.x, position_.y)
            state_description = 'caso 1 - distanciaGrande1'
            change_state(7)
        elif regions['front'] >= 13.137 and regions['front'] < 15.737 and position_.x - desired_position_.x >= 0.96 and position_.y - desired_position_.y >= 0.96 and position_.x - desired_position_.x < 1.04 and position_.y - desired_position_.y < 1.04:
            rospy.loginfo("Position: [%.2f, %.2f]",position_.x, position_.y)
            state_description = 'caso 1 - distanciaGrande2'
            change_state(8)
        elif regions['front'] >= 13.137 and regions['front'] < 15.737 and position_.x - desired_position_.x >= 0.697 and position_.y - desired_position_.y >= 0.697 and position_.x - desired_position_.x < 0.96 and position_.y - desired_position_.y < 0.96: 
            rospy.loginfo("Position: [%.2f, %.2f]",position_.x, position_.y)
            state_description = 'caso 1 - distanciaGrande2'
            change_state(8)
        elif regions['front'] >= 13.137 and regions['front'] < 15.737 and position_.x - desired_position_.x >= 1.04 and position_.y - desired_position_.y >= 1.04 and position_.x - desired_position_.x < 1.36 and position_.y - desired_position_.y < 1.36: 
            rospy.loginfo("Position: [%.2f, %.2f]",position_.x, position_.y)
            state_description = 'caso 1 - distanciaGrande2'
            change_state(8)
        elif regions['front'] >= 15.737 and regions['front'] <= 20.137 and position_.x - desired_position_.x >= 1.04 and position_.y - desired_position_.y >= 1.04 and position_.x - desired_position_.x < 1.36 and position_.y - desired_position_.y < 1.36:
            rospy.loginfo("Position: [%.2f, %.2f]",position_.x, position_.y)
            state_description = 'caso 1 - distanciaGrande3'
            change_state(9)
        elif regions['front'] >= 15.737 and regions['front'] <= 20.137 and position_.x - desired_position_.x >= 0.96 and position_.y - desired_position_.y >= 0.96 and position_.x - desired_position_.x < 1.04 and position_.y - desired_position_.y < 1.04:
            rospy.loginfo("Position: [%.2f, %.2f]",position_.x, position_.y)
            state_description = 'caso 1 - distanciaGrande3'
            change_state(9)
        elif regions['front'] >= 15.737 and regions['front'] <= 20.137 and position_.x - desired_position_.x >= 0.697 and position_.y - desired_position_.y >= 0.697 and position_.x - desired_position_.x < 0.96 and position_.y - desired_position_.y < 0.96:
            rospy.loginfo("Position: [%.2f, %.2f]",position_.x, position_.y)
            state_description = 'caso 1 - distanciaGrande3'
            change_state(9)