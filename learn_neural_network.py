import re


def lemma_message(message, morph = None):
	"""
	Лемматизировать сообщение

	Args:
		message (string): сообщение

	Returns:
		(string): лемматизированное сообщение
	"""
	if not morph:
		morph = pymorphy2.MorphAnalyzer()
	lemma = []
	message = message.lower()
	message = message.strip()
	message = re.sub(r"\s{2:}", " ", message)
	message = re.sub(r"[\(\)\{\}\[\],\.:;\+\-]", "", message)
	for word in message.split(" "):
		res = morph.parse(word)[0]
		if res.normal_form:
			res = res.normal_form
		else:
			res = word 
		lemma.append(res)
	return " ".join(lemma)