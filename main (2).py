# Define the base class player 
class player:
  def play(self):
    print("The player is playing cricket.")
    
# Define the derived class batsman
class Batsman(player):
  def play(self):
    print("The batsam is batting.")

# Define the derived class bowler
class Bowler(player):
  def play(self):
      print("The bowler is bowling.")
    
# Create object of Batsman and Bowler Classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object 
batsman.play()
bowler.play()