import pygame
from Button import Button

class Ghosts:
	def __init__(self):
		self.banshee = Button((255, 178, 102), 0, 0, "BANSHEE")
		self.demon = Button((255, 178, 102), 0, 130, "DEMON")
		self.goryo = Button((255, 178, 102), 0, 260, "GORYO")
		self.hantu = Button((255, 178, 102), 0, 390, "HANTU")
		self.jinn = Button((255, 178, 102), 0, 520, "JINN")
		self.mare = Button((255, 178, 102), 0, 650, "MARE") 
		self.myling = Button((255, 178, 102), 0, 780, "MYLING")
		self.obake = Button((255, 178, 102), 200, 0, "OBAKE")
		self.oni = Button((255, 178, 102), 200, 130, "ONI")
		self.onryo = Button((255, 178, 102), 200, 260, "ONRYO")
		self.phantom = Button((255, 178, 102), 200, 390, "PHANTOM")
		self.polter = Button((255, 178, 102), 200, 520, "POLTERGEIST")
		self.raiju = Button((255, 178, 102), 200, 650, "RAIJU")
		self.rev = Button((255, 178, 102), 200, 780, "REVENANT")
		self.shade = Button((255, 178, 102), 400, 0, "SHADE")
		self.spirit = Button((255, 178, 102), 400, 130, "SPIRIT")
		self.mimic = Button((255, 178, 102), 400, 260, "THE MIMIC")
		self.twins = Button((255, 178, 102), 400, 390, "THE TWINS")
		self.wraith = Button((255, 178, 102), 400, 520, "WRAITH")
		self.yokai = Button((255, 178, 102), 400, 650, "YOKAI")
		self.yurei = Button((255, 178, 102), 400, 780, "YUREI")

		self.bansheeInfo = [
			"Banshee",
			" ",
			"Ways To Test:",
			"   - Targets one person until they die",
			"   - Will be a normal ghost if its target leaves",
			"     the place",
			"   - Crucifix has a greater range",
			" ",
			" ",
			"Evidence:",
			"   - Fingerprints",
			"   - Ghost Orb",
			"   - D.O.T.S Projector"
		]

		self.demonInfo = [
			"Demon",
			" ",
			"Ways To Test:",
			"   - ",
			" ",
			" ",
			"Evidence:",
			"   - ",
			"   - ",
			"   - "
		]

		self.goryoInfo = [
			"Goryo",
			" ",
			"Ways To Test:",
			"   - Will show DOTS only if no one is in the",
			"     same room",
			"   - Always has D.O.T.S Projector",
			"   - Roams less than other ghosts",
			" ",
			" ",
			"Evidence:",
			"   - EMF Level 5",
			"   - Fingerprints",
			"   - D.O.T.S Projector"
		]

		self.hantuInfo = [
			"Hantu",
			" ",
			"Ways To Test:",
			"   - Snow/rainstorm/breaker affects the",
			"     temperature in the map",
			"   - The colder, the faster",
			"   - Never speeds up during a hunt",
			"   - Always has freezing temperatures",
			"   - Will have freezing breath if in a freezing room",
			" ",
			" ",
			"Evidence:",
			"   - Fingerprints",
			"   - Ghost Orb",
			"   - Freezing Temperature"
		]

		self.jinnInfo = [
			"Jinn",
			" ",
			"Ways To Test:",
			"   - Cannot turn off the breaker",
			"   - Faster when further away from players",
			"     and gets slower as it approaches,",
			"     but still can catch up (only applies when",
			"     breaker is off)",
			"   - Chance to drop sanity by 25 if close enough",
			" ",
			" ",
			"Evidence:",
			"   - EMF Level 5",
			"   - Fingerprints",
			"   - Freezing Temperature"
		]

		self.mareInfo = [
			"Mare",
			" ",
			"Ways To Test:",
			"   - Cannot turn lights off",
			"   - Can hunt at 60 sanity if light is off, 40 if on",
			" ",
			" ",
			"Evidence:",
			"   - ",
			"   - ",
			"   - "
		]

		self.mylingInfo = [
			"Myling",
			" ",
			"Ways To Test:",
			"   - Only footsteps are quieter",
			"   - Flashlight blinks before you hear the footsteps",
			"     during a hunt (Raiju can also do this)",
			" ",
			" ",
			"Evidence:",
			"   - EMF Level 5",
			"   - Fingerprints",
			"   - Ghost Writing"
		]

		self.obakeInfo = [
			"Obake",
			" ",
			"Ways To Test:",
			"   - ",
			" ",
			" ",
			"Evidence:",
			"   - ",
			"   - ",
			"   - "
		]

		self.oniInfo = [
			"Oni",
			" ",
			"Ways To Test:",
			"   - ",
			" ",
			" ",
			"Evidence:",
			"   - ",
			"   - ",
			"   - "
		]

		self.onryoInfo = [
			"Onryo",
			" ",
			"Ways To Test:",
			"   - Can hunt right after the ghost blows out",
			"     a candle (only one candle)",
			"   - Possibility of hunting after blowing a candle",
			"     increases as players die",
			"   - Blows candles more often",
			"   - Candles act as Crucifix (Priority over Crucifix)",
			"   - Can hunt at 60 sanity if no candles are nearby",
			" ",
			" ",
			"Evidence:",
			"   - Spirit Box",
			"   - Ghost Orb",
			"   - Freezing Temperature"
		]

		self.phantomInfo = [
			"Phantom",
			" ",
			"Ways To Test:",
			"   - Can roam to any player",
			"   - Blinks less frequent during a hunt",
			"   - Looking at the ghost drains sanity faster",
			"   - When you take a picture and you go to the journal,",
			"     it will not show up in the picture but will count",
			"     as a ghost photo",
			" ",
			" ",
			"Evidence:",
			"   - Spirit Box",
			"   - Fingerprints",
			"   - D.O.T.S Projector"
		]

		self.polterInfo = [
			"Poltergiest",
			" ",
			"Ways To Test:",
			"   - Can throw multiple things at the same time (0 to 10",
			"     spike in the activity chart)",
			"   - Witnessing multi-throw will drain sanity",
			"   - Can do faster throws",
			" ",
			" ",
			"Evidence:",
			"   - Spirit Box",
			"   - Fingerprints",
			"   - Ghost Writing"
		]

		self.raijuInfo = [
			"Raiju",
			" ",
			"Ways To Test:",
			"   - ",
			" ",
			" ",
			"Evidence:",
			"   - ",
			"   - ",
			"   - "
		]

		self.revInfo = [
			"Revenant",
			" ",
			"Ways To Test:",
			"   - ",
			" ",
			" ",
			"Evidence:",
			"   - ",
			"   - ",
			"   - "
		]

		self.shadeInfo = [
			"Shade",
			" ",
			"Ways To Test:",
			"   - ",
			" ",
			" ",
			"Evidence:",
			"   - ",
			"   - ",
			"   - "
		]

		self.spiritInfo = [
			"Spirit",
			" ",
			"Ways To Test:",
			"   - Only hunts 180 seconds after being smudged",
			" ",
			" ",
			"Evidence:",
			"   - EMF Level 5",
			"   - Spirit Box",
			"   - Ghost Writing"
		]

		self.mimicInfo = [
			"The Mimic",
			" ",
			"Ways To Test:",
			"   - ",
			" ",
			" ",
			"Evidence:",
			"   - ",
			"   - ",
			"   - "
		]

		self.twinsInfo = [
			"The Twins",
			" ",
			"Ways To Test:",
			"   - Decoy cannot do spirit box or lower temperature",
			"   - During a hunt, decoy is 110 percent faster,",
			"     real is 90 percent",
			"   - Sound sensors can be used to pick up twin",
			"     sounds (over 0.1)",
			"   - Can do interactions 1 second apart",
			"   - Slope change in activity chart",
			"   - Decoy hunts start from decoy interaction",
			" ",
			" ",
			"Evidence:",
			"   - EMF Level 5",
			"   - Spirit Box",
			"   - Freezing Temperature"
		]

		self.wraithInfo = [
			"Wraith",
			" ",
			"Ways To Test:",
			"   - Can teleport to any player",
			"   - Does not have footprints",
			"   - ",
			" ",
			" ",
			"Evidence:",
			"   - EMF Level 5",
			"   - Spirit Box",
			"   - D.O.T.S Projector"
		]

		self.yokaiInfo = [
			"Yokai",
			" ",
			"Ways To Test:",
			"   - Can hunt below 80 sanity if you talk while",
			"     on top of the ghost",
			"   - Can hunt very close to you",
			"   - If out of sight during a hunt, it might not",
			"     be able to hear you if you talk to it",
			" ",
			" ",
			"Evidence:",
			"   - Spirit Box",
			"   - Ghost Orb",
			"   - D.O.T.S Projector"
		]

		self.yureiInfo = [
			"Yurei",
			" ",
			"Ways To Test:",
			"   - ",
			" ",
			" ",
			"Evidence:",
			"   - ",
			"   - ",
			"   - "
		]

	def getGhosts(self):
		return [
			self.banshee,
			self.demon,
			self.goryo,
			self.hantu,
			self.jinn,
			self.mare,
			self.myling,
			self.obake,
			self.oni,
			self.onryo,
			self.phantom,
			self.polter,
			self.raiju,
			self.rev,
			self.shade,
			self.spirit,
			self.mimic,
			self.twins,
			self.wraith,
			self.yokai,
			self.yurei
		]

	def getInfo(self):
		return [
			self.bansheeInfo,
			self.demonInfo,
			self.goryoInfo,
			self.hantuInfo,
			self.jinnInfo,
			self.mareInfo,
			self.mylingInfo,
			self.obakeInfo,
			self.oniInfo,
			self.onryoInfo,
			self.phantomInfo,
			self.polterInfo,
			self.raijuInfo,
			self.revInfo,
			self.shadeInfo,
			self.spiritInfo,
			self.mimicInfo,
			self.twinsInfo,
			self.wraithInfo,
			self.yokaiInfo,
			self.yureiInfo
		]