import pygame
from Button import Button

class Ghosts:
	def __init__(self):
		self.spirit = Button((255, 178, 102), 0, 0, 200, 130, "SPIRIT")
		self.polter = Button((255, 178, 102), 0, 130, 200, 130, "POLTERGEIST")
		self.mare = Button((255, 178, 102), 0, 260, 200, 130, "MARE")
		self.demon = Button((255, 178, 102), 0, 390, 200, 130, "DEMON")
		self.yokai = Button((255, 178, 102), 0, 520, 200, 130, "YOKAI")
		self.myling = Button((255, 178, 102), 0, 650, 200, 130, "MYLING") 
		self.raiju = Button((255, 178, 102), 0, 780, 200, 130, "RAIJU")
		self.wraith = Button((255, 178, 102), 200, 0, 200, 130, "WRAITH")
		self.banshee = Button((255, 178, 102), 200, 130, 200, 130, "BANSHEE")
		self.rev = Button((255, 178, 102), 200, 260, 200, 130, "REVENANT")
		self.yurei = Button((255, 178, 102), 200, 390, 200, 130, "YUREI")
		self.hantu = Button((255, 178, 102), 200, 520, 200, 130, "HANTU")
		self.onryo = Button((255, 178, 102), 200, 650, 200, 130, "ONRYO")
		self.obake = Button((255, 178, 102), 200, 780, 200, 130, "OBAKE")
		self.phantom = Button((255, 178, 102), 400, 0, 200, 130, "PHANTOM")
		self.jinn = Button((255, 178, 102), 400, 130, 200, 130, "JINN")
		self.shade = Button((255, 178, 102), 400, 260, 200, 130, "SHADE")
		self.oni = Button((255, 178, 102), 400, 390, 200, 130, "ONI")
		self.goryo = Button((255, 178, 102), 400, 520, 200, 130, "GORYO")
		self.twins = Button((255, 178, 102), 400, 650, 200, 130, "THE TWINS")
		self.mimic = Button((255, 178, 102), 400, 780, 200, 130, "THE MIMIC")

		self.bansheeInfo = [
			"Banshee",
			" ",
			"Ways To Test:",
			"   - Targets one person until they die",
			"   - Will be a normal ghost if its target leaves",
			"     the place",
			"   - Crucifix has a greater range",
			"   - Prefers to do singing ghost events",
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
			"   - Can hunt at 70 sanity unless it has the",
			"   - Banshee ability where it can hunt at 100",
			"   - Hunts more than other ghosts",
			"   - 20 second cooldown for hunts without smudging",
			"   - 60 second cooldown for hunts after smudging",
			" ",
			" ",
			"Evidence:",
			"   - Fingerprints",
			"   - Ghost Writing",
			"   - Freezing Temperatures"
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
			"   - Freezing Temperatures"
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
			"   - Freezing Temperatures"
		]

		self.mareInfo = [
			"Mare",
			" ",
			"Ways To Test:",
			"   - Can turn lights off, not on",
			"   - Can hunt at 60 sanity if light is off, 40 if on",
			"   - Prefers to do light exploding ghost events",
			"   - May roam further if the light is on in the room",
			" ",
			" ",
			"Evidence:",
			"   - Spirit Box",
			"   - Ghost Orb",
			"   - Ghost Writing"
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
			"   - Chance to not leave fingerprints",
			"   - May show 6 fingers in the fingerprint",
			"   - Fingerprints can disappear quickly",
			"	- Always has fingerprints",
			" ",
			" ",
			"Evidence:",
			"   - EMF Level 5",
			"   - Fingerprints",
			"   - Ghost Orb"
		]

		self.oniInfo = [
			"Oni",
			" ",
			"Ways To Test:",
			"   - More interactions and ghost events",
			"   - Throws objects further and faster",
			"   - Prefers physical form ghost events",
			"   - Never does the airball ghost event",
			" ",
			" ",
			"Evidence:",
			"   - EMF Level 5",
			"   - Freezing Temperatures",
			"   - D.O.T.S Projector"
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
			"   - Freezing Temperatures"
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
			"   - Can hunt at 65 sanity if electronic equipment",
			"     are nearby",
			"   - Faster if electronic equipment are nearby",
			" ",
			" ",
			"Evidence:",
			"   - EMF Level 5",
			"   - Ghost Orb",
			"   - D.O.T.S Projector"
		]

		self.revInfo = [
			"Revenant",
			" ",
			"Ways To Test:",
			"   - Fastest ghost when in line of sight",
			"   - Very slow when not chasing a player",
			" ",
			" ",
			"Evidence:",
			"   - Ghost Orb",
			"   - Ghost Writing",
			"   - Freezing Temperatures"
		]

		self.shadeInfo = [
			"Shade",
			" ",
			"Ways To Test:",
			"   - Can only hunt at 35 sanity",
			"   - Prefers to do airball or shadow ghost events",
			"   - Can never hunt when multiple people are",
			"   - nearby the ghost",
			" ",
			" ",
			"Evidence:",
			"   - EMF Level 5",
			"   - Ghost Writing",
			"   - Freezing Temperatures"
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
			"   - Mimics one ghost and its abilities at a time",
			" ",
			" ",
			"Evidence:",
			"   - Spirit Box",
			"   - Fingerprints",
			"   - Freezing Temperatures"
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
			"   - Freezing Temperatures"
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
			"   - Chance to drop 13 sanity and fully close",
			"     a door nearby",
			"   - Cannot leave the room after smudging",
			" ",
			" ",
			"Evidence:",
			"   - Ghost Orb",
			"   - Freezing Temperatures",
			"   - D.O.T.S Projector"
		]

		self.spiritEvid = [
			"box",
			"emf",
			"writing"
		]

		self.polterEvid = [
			"box",
			"finger",
			"writing"
		]

		self.mareEvid = [
			"box",
			"orb",
			"writing"
		]

		self.demonEvid = [
			"finger",
			"writing",
			"freezing"
		]

		self.yokaiEvid = [
			"box",
			"orb",
			"dots"
		]

		self.mylingEvid = [
			"emf",
			"finger",
			"writing"
		]

		self.raijuEvid = [
			"emf",
			"orb",
			"dots"
		]

		self.wraithEvid = [
			"emf",
			"box",
			"dots"
		]

		self.bansheeEvid = [
			"finger",
			"orb",
			"dots"
		]

		self.revEvid = [
			"orb",
			"writing",
			"freezing"
		]

		self.yureiEvid = [
			"orb",
			"freezing",
			"dots"
		]

		self.hantuEvid = [
			"finger",
			"orb",
			"freezing"
		]

		self.onryoEvid = [
			"box",
			"orb",
			"freezing"
		]

		self.obakeEvid = [
			"emf",
			"finger",
			"orb"
		]

		self.phantomEvid = [
			"box",
			"finger",
			"dots"
		]

		self.jinnEvid = [
			"emf",
			"finger",
			"freezing"
		]

		self.shadeEvid = [
			"emf",
			"writing",
			"freezing"
		]

		self.oniEvid = [
			"emf",
			"freezing",
			"dots"
		]

		self.goryoEvid = [
			"emf",
			"finger",
			"dots"
		]

		self.twinsEvid = [
			"emf",
			"box",
			"freezing"
		]

		self.mimicEvid = [
			"box",
			"finger",
			"freezing"
		]


	def getGhosts(self):
		return [
			self.spirit,
			self.polter,
			self.mare,
			self.demon,
			self.yokai,
			self.myling,
			self.raiju,
			self.wraith,
			self.banshee,
			self.rev,
			self.yurei,
			self.hantu,
			self.onryo,
			self.obake,
			self.phantom,
			self.jinn,
			self.shade,
			self.oni,
			self.goryo,
			self.twins,
			self.mimic
		]

	def getInfo(self):
		return [
			self.spiritInfo,
			self.polterInfo,
			self.mareInfo,
			self.demonInfo,
			self.yokaiInfo,
			self.mylingInfo,
			self.raijuInfo,
			self.wraithInfo,
			self.bansheeInfo,
			self.revInfo,
			self.yureiInfo,
			self.hantuInfo,
			self.onryoInfo,
			self.obakeInfo,
			self.phantomInfo,
			self.jinnInfo,
			self.shadeInfo,
			self.oniInfo,
			self.goryoInfo,
			self.twinsInfo,
			self.mimicInfo
		]

	def getEvidence(self):
		return [
			self.spiritEvid,
			self.polterEvid,
			self.mareEvid,
			self.demonEvid,
			self.yokaiEvid,
			self.mylingEvid,
			self.raijuEvid,
			self.wraithEvid,
			self.bansheeEvid,
			self.revEvid,
			self.yureiEvid,
			self.hantuEvid,
			self.onryoEvid,
			self.obakeEvid,
			self.phantomEvid,
			self.jinnEvid,
			self.shadeEvid,
			self.oniEvid,
			self.goryoEvid,
			self.twinsEvid,
			self.mimicEvid
		]