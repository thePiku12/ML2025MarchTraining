data = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}

print("Here is your complete Data Enjoy: ",data)
print("Here are your keys from the data: ",data.keys())
print("Here are your corosponding values of the key from the data: ",data.values())
print("GlossTerm: ", data["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]['GlossTerm'])
print("GlossDef: ", data["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]['GlossDef'])
print("GlossDef GlossSeeAlso at 2: ", data["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]['GlossDef']["GlossSeeAlso"][1])