unicodes = [
	u'\u2070',	# hoch 0
	u'\u00B9',	# hoch 1
	u'\u00B2',	# hoch 2
	u'\u00B3',	# hoch 3
	u'\u2074',	# hoch 4
	u'\u2075',	# hoch 5
	u'\u2076',	# hoch 6
	u'\u2077',	# hoch 7
	u'\u2078',	# hoch 8
	u'\u2079'];	# hoch 9



class Alpha:
	

	def __init__(self, gf, number):
		self.gf = gf;
		self.isNull = number is None;
		self.vector = [0 for a in self.gf[0]];
		if not self.isNull:
			self.number = number;
			self.alpha = "".join([u'\u03B1'] + [unicodes[int(i)] for i in str(number)]);
			self.vector = [int(a) for a in self.gf[self.number]];
		
	
	def __repr__(self):
		return ''.join(str(i) for i in self.vector);

	def __str__(self):		
		return ''.join(str(i) for i in self.vector);
	
	def getAlpha(self):
		return self.alpha if not self.isNull else '0';

	def __add__(self, summand):
		vector = [(self.vector[i] + summand.vector[i]) % 2 for i in range(len(self.vector))];
		if 1 not in vector:
			return Alpha(self.gf, None);
		s = "".join([str(a) for a in vector]);
		return Alpha(self.gf, self.gf.index(s));

	def __eq__(self, eq):
		return self.getAlpha() and eq.getAlpha() and str(self) == str(eq) and self.gf == eq.gf;

	def __mul__(self, factor):
		product = (self.number + factor.number) % len(self.gf);
		return Alpha(self.gf, product);

	def __neg__(self):
		return Alpha(self.gf, -self.number % len(self.gf));
		
	def __len__(self):
		return len(self.gf[self.number]);

	def __getitem__(self, item):
		return int(self.gf[self.number][item]);
