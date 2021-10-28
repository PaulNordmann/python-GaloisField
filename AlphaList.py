from Alpha import Alpha;
from modPol import modPols;


def getAlphas(modPol):
	if modPol not in modPols:
		print 'modular polynomials:\n' + '\n\t'.join([''] + modPols + ['']); 
		raise NameError('not a modular polynomial');

	l = len(modPol) - 1
		
	exp = 2**l;
	alphas = [1]
	mod = int(modPol, 2);
	while len(alphas) < exp:
		next = alphas[-1] << 1
		if next >= exp:
			next = next ^ mod;
		alphas.append(next);
		if next == alphas[0]:
			break;

	if alphas.pop() != alphas[0]:
		raise NameError('Problems with the modular polynom');
	strAlphas = [];
	for value in alphas:
		s = str(bin(value))[2:];
		strAlphas.append( "".join(["0" for i in range(l - len(s))]) + s);
	return strAlphas;

def AlphaList(modPol):
	tmp = getAlphas(modPol);
	return [Alpha(tmp, i) for i, a in enumerate(tmp)];	
