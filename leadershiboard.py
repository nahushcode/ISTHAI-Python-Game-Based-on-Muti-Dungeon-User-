import gameplay


class leadershipboard:
      def __init__(self):
       @classmethod
       def register(cls):
          cls.username = gameplay.player.score
          cls.password = gameplay.player.name
          file = open("leadershipboard.txt.txt", "a")
          file.write(cls.username)
          file.write(" ")
          file.write("    ")
          file.write(cls.password)
          file.write("\n")
          file.close()




playerform = registeration(a1)
playerform.register()