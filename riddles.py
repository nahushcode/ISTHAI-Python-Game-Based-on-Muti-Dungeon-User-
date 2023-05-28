# creating a riddles for the game



class riddles:
      def __init__(self,message):
                self.message = message



      @classmethod
      def riddle1(cls,message):
         cls.message = message
         print('Yakasa appeared ')
         print('Yaksha --> To pass this gate answer my questions ohh son of saphein ' )
         print('Yakshya --> who is really a helpful companion and always be with you ')
         print('1 -> Steady Intelligence ')
         print('2->   Loyal Friend')
         print('3 ->  No one')
         user_input = input("Enter your preference")
         if user_input == '1':
                print("that'correct son of saphien --> you have passed ")
                fight()
         elif user_input == '3':
              pass
         else:
              pass

      @classmethod
      def riddle2(cls):
           cls.message = message
           print('Yakasa appeared ')
           print('Yaksha --> ohh son of saphein -> To pass this gate -> answer my questions  ' )
           print('Yakshya --> What makes person a true hero ? ')
           print('1 -> Super Powers')
           print('2->  Acknowledgement of others')
           print('3 -> Will to risk their own life to save other')
           user_input = input("Enter your preference")
           if user_input == '1':
              pass
           elif user_input == '2':
                pass
           elif user_input == '3':
                pass
           else:
                pass

      @classmethod
      def riddle3(cls):
             cls.message = message
             print('Yakasa appeared ')
             print('Yaksha --> To pass this gate answer my questions ohh son of saphein ' )
             print('Yakshya --> What makes person a true Leader ? ')
             print('1 -> Bossy Attitude')
             print('2->  Supremacy over others')
             print('3 -> Sense of responsibility')
             user_input = input("Enter your preference")
             if user_input == '1':
                pass
             elif user_input == '2':
                pass
             elif user_input == '3':
                pass
             else:
                pass

      @classmethod
      def riddle4(cls):
             self.message = message
             print('Yakasa appeared ')
             print('Yaksha --> To pass this gate  answer my questions ohh son of saphein ' )
             print('Yakshya --> Which is the most important quality inside the human? ')
             print('1 -> GREED')
             print('2->  Love For Others')
             print('3 -> Over Competative Nature ')
             user_input = input("Enter your preference")
             if user_input == '1':
                pass
             elif user_input == '2':
                pass
             elif user_input == '3':
                  pass
             else:
                  pass
      @classmethod
      def riddle5(self):
           self.message = message
           print('Yakasa appeared ')
           print('Yaksha --> To pass this gate answer my questions ohh son of saphein ')
           print('Yakshya --> What is Freedom? ')
           print('1 -> Want to leave this world and go back to earth')
           print('2->  Control over other dependence')
           print('3 -> Freedom from unecessary desires ')
           user_input = input("Enter your preference")
           if user_input == '1':
               pass
           elif user_input == '2':
               pass
           elif user_input == '3':
               pass
           else:
               pass
      @classmethod
      def riddle6():
           print('Yakasa appeared ')
           print('Yaksha --> To pass this gate  answer my questions ohh son of saphein ')
           print('Yakshya --> When people start enjoy doing their work? ')
           print('1 -> Work with rewards')
           print('2->  Work with good team')
           print('3 -> Work without desires ')
           user_input = input("Enter your preference")
           if user_input == '1':
               pass
           elif user_input == '2':
               pass
           elif user_input == '3':
               pass
           else:
               pass



message = input('Call Yaksha ')
riddler = riddles(message)
riddler.riddle1(message)
