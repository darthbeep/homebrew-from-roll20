import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import simple_conversion

inputs = []

inputs.append({
			"attributes": {
				"name": "Wand of Magic Missiles",
				"notes": 1507682059099,
				"avatar": "https://s3.amazonaws.com/files.d20.io/images/40505962/vLK8JVi7WGQCO6eWakKtJQ/med.png?1507682059",
				"inplayerjournals": "",
				"archived": False,
				"tags": "[]",
				"controlledby": "",
				"id": "-Kw7paEAQl6NcSVpF5ix"
			},
			"blobNotes": "%3Ch4%3EWand%20of%20Magic%20Missiles%3C/h4%3E%3Cem%3EWand%2C%20uncommon%3Cbr%3E%3C/em%3E%3Cbr%3EThis%20wand%20has%207%20charges.%20With%20the%20wand%20in%20hand%2C%20you%20can%20use%20your%20action%20to%20fire%20the%20%3Cem%3Emagic%20missile%3C/em%3E%20spell%20from%20the%20wand%u2014no%20components%20required%u2014and%20expend%201%20to%203%20of%20the%20wand%u2019s%20charges.%20For%20each%20charge%20you%20expend%20beyond%201%2C%20the%20spell%u2019s%20level%20increases%20by%201.%20You%20can%20use%20this%20wand%20even%20if%20you%20are%20incapable%20of%20casting%20spells.%3Cbr%3E%3Cbr%3EThe%20wand%20regains%201d6%20+%201%20expended%20charges%20each%20day%20at%20dawn.%20If%20you%20expend%20the%20wand%u2019s%20last%20charge%2C%20roll%20a%20d20.%20On%20a%201%2C%20the%20wand%20crumbles%20into%20ash%20and%20is%20destroyed.",
			"blobGmNotes": ""
		})

simple_conversion.create_item(inputs[0])