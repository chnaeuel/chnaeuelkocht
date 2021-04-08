AMOUNT = [
    i
    for i in range(1, 1000)
    if i < 11 or (i < 100 and i % 10 == 0) or (i < 1000 and i % 50 == 0) or i == 1000
]

# Second element indicates if we should inflect
UNIT = [
    (("Beutel",), True),
    (("cl",), False),
    (("cm",), False),
    (("cup", "cups"), False),
    (("dl",), False),
    (("EL",), False),
    (("g",), False),
    (("kg",), False),
    (("Kiste", "Kisten"), True),
    (("Liter",), False),
    (("Löffel",), False),
    (("Messerspitze", "Messerspitzen"), False),
    (("Meter",), False),
    (("oz",), False),
    (("Pack",), True),
    (("Prise", "Prisen"), False),
    (("Scheiben",), False),
    (("Stück",), True),
    (("TL",), False),
]

# Second element indicates if we should inflect. Higher priority than UNIT inflection
FOOD = [
    (("Aalsuppe",), False),
    (("Agavendicksaft",), False),
    (("Ahornsirup", "Ahornsirupe"), False),
    (("Ajvar",), False),
    (("Ananas", "Ananas"), False),
    (("Anis",), False),
    (("Anona",), False),
    (("Apfel", "Äpfel"), False),
    (("Apfelkompott", "Apfelkompotte"), False),
    (("Apfelkraut",), False),
    (("Apfelsine", "Apfelsinen"), False),
    (("Aprikose", "Aprikosen"), False),
    (("Artischocke", "Artischocken"), False),
    (("Artischockenherz",), False),
    (("Aubergine", "Auberginen"), False),
    (("Auflauf", "Aufläufe"), False),
    (("Austernpilz", "Austernpilze"), True),
    (("Avocado", "Avocados"), False),
    (("Backaroma", "Backaromen"), False),
    (("Backfett", "Backfette"), False),
    (("Backware", "Backwaren"), False),
    (("Backwerk", "Backwerke"), False),
    (("Baiser", "Baisers"), False),
    (("Balsamessig",), False),
    (("Balsamico", "Balsamicos"), False),
    (("Banane", "Bananen"), False),
    (("Basilikum", "Basiliken"), False),
    (("Bauernbrot", "Bauernbrote"), False),
    (("Bergkäse",), False),
    (("Bienenstich", "Bienenstiche"), False),
    (("Bier", "Biere"), False),
    (("Birne", "Birnen"), False),
    (("Biskuitteig",), False),
    (("Bitterschokolade", "Bitterschokoladen"), False),
    (("Blattsalat", "Blattsalate"), False),
    (("Blattspinat", "Blattspinate"), False),
    (("Blaubeere", "Blaubeeren"), True),
    (("Blaukohl",), False),
    (("Blaukraut",), False),
    (("Blauschimmelkäse", "Blauschimmelkäse"), False),
    (("Blätterteig",), False),
    (("Blumenkohl",), False),
    (("Blutorange", "Blutorangen"), False),
    (("Blutwurst", "Blutwürste"), False),
    (("Blütenhonig",), False),
    (("Bockwurst", "Bockwürste"), False),
    (("Bohne", "Bohnen"), False),
    (("Bohnenkraut", "Bohnenkräuter"), False),
    (("Bohnensuppe",), False),
    (("Borschtsch",), False),
    (("Boskop", "Boskop"), False),
    (("Bouillon", "Bouillons"), False),
    (("Bouillonwürfel", "Bouillonwürfel"), False),
    (("Bratapfel", "Bratäpfel"), False),
    (("Bratwurst", "Bratwürste"), False),
    (("Broccoli", "Broccoli"), False),
    (("Brokkoli", "Brokkoli"), False),
    (("Brombeere", "Brombeeren"), True),
    (("Brot", "Brote"), False),
    (("Brotaufstrich",), False),
    (("Brotsuppe",), False),
    (("Brotteig",), False),
    (("Brunnenkresse", "Brunnenkressen"), False),
    (("Brühwürfel", "Brühwürfel"), False),
    (("Buchweizen",), False),
    (("Bulgur",), False),
    (("Butter",), False),
    (("Buttercreme",), False),
    (("Buttergebäck",), False),
    (("Butterkäse", "Butterkäse"), False),
    (("Butterkeks", "Butterkekse"), True),
    (("Butterpilz", "Butterpilze"), True),
    (("Büchsenmilch",), False),
    (("Béchamelsauce", "Béchamelsaucen"), False),
    (("Calzone", "Calzones"), False),
    (("Camembert", "Camemberts"), False),
    (("Cannelloni", "Cannellonis"), False),
    (("Cashew", "Cashews"), True),
    (("Cashewnuss", "Cashewnüsse"), True),
    (("Cayennepfeffer", "Cayennepfeffer"), False),
    (("Champignon", "Champignons"), True),
    (("Cheddarkäse", "Cheddarkäse"), False),
    (("Chesterkäse",), False),
    (("Chiasamen",), True),
    (("Chicken Nugget", "Chicken Nuggets"), False),
    (("Chicorée", "Chicorées"), False),
    (("Chili", "Chilis"), False),
    (("Chilisauce", "Chilisaucen"), False),
    (("Chinakohl",), False),
    (("Chip", "Chips"), True),
    (("Chorizo", "Chorizos"), False),
    (("Christstollen", "Christstollen"), False),
    (("Ciabatta", "Ciabattas"), False),
    (("Citrusfrucht", "Citrusfrüchte"), False),
    (("Clementine", "Clementinen"), False),
    (("Consommé",), False),
    (("Cookie", "Cookies"), True),
    (("Corned beef",), False),
    (("Cornflake", "Cornflakes"), False),
    (("Couscous",), False),
    (("Cranberry", "Cranberrys"), True),
    (("Croissant", "Croissants"), False),
    (("Crème fraîche",), False),
    (("Curry", "Currys"), False),
    (("Currypulver",), False),
    (("Currysauce", "Currysaucen"), False),
    (("Currywurst", "Currywürste"), False),
    (("Dattel", "Datteln"), False),
    (("Dattelpflaume", "Dattelpflaumen"), True),
    (("Datteltraube", "Datteltrauben"), True),
    (("Dauerwurst", "Dauerwürste"), False),
    (("Deichkäse",), False),
    (("Delikatessgurke", "Delikatessgurken"), True),
    (("Delikatesssenf", "Delikatesssenfe"), False),
    (("Dessert", "Desserts"), False),
    (("Diätzucker",), False),
    (("Dickmilch",), False),
    (("Dill", "Dille"), False),
    (("Dinkel", "Dinkel"), False),
    (("Dinkelmehl",), False),
    (("Distelöl", "Distelöle"), False),
    (("Dominostein", "Dominosteine"), False),
    (("Dosenfleisch",), False),
    (("Dosenmilch",), False),
    (("Dosensuppe",), False),
    (("Dosenwurst", "Dosenwürste"), False),
    (("Döner", "Döner"), False),
    (("Dörrfleisch",), False),
    (("Dörrgemüse",), False),
    (("Dörrobst",), False),
    (("Dörrpflaume", "Dörrpflaumen"), True),
    (("Dressing",), False),
    (("Drops", "Dropse"), False),
    (("Edamer", "Edamer"), False),
    (("Edamer Käse",), False),
    (("Edelpilzkäse",), False),
    (("Ei", "Eier"), False),
    (("Eierkuchen", "Eierkuchen"), False),
    (("Eigelb", "Eigelbe"), False),
    (("Einbrennsuppe",), False),
    (("Eingemachtes",), False),
    (("Eingetropftes",), False),
    (("Eintopf", "Eintöpfe"), False),
    (("Eis", "Eis"), False),
    (("Eisbergsalat", "Eisbergsalate"), False),
    (("Emmentaler", "Emmentaler"), False),
    (("Ente", "Enten"), False),
    (("Entenbrust", "Entenbrüste"), False),
    (("Erbse", "Erbsen"), True),
    (("Erbsensuppe",), False),
    (("Erdbeere", "Erdbeeren"), True),
    (("Erdbeergelée", "Erdbeergelées"), False),
    (("Erdnuss", "Erdnüsse"), False),
    (("Erdnussbutter",), False),
    (("Erdnussflip", "Erdnussflips"), True),
    (("Erdnussmus",), False),
    (("Erdnussöl",), False),
    (("Essig", "Essige"), False),
    (("Essiggurke", "Essiggurken"), True),
    (("Esskastanie", "Esskastanien"), False),
    # (("Esswaren",), False),
    (("Estragon",), False),
    (("Feige", "Feigen"), True),
    (("Feinbackwaren",), False),
    (("Feingebäck",), False),
    (("Feinkost",), False),
    (("Felchen",), False),
    (("Feldbohne", "Feldbohnen"), True),
    (("Feldfrucht", "Feldfrüchte"), True),
    (("Feldsalat", "Feldsalate"), False),
    (("Fenchel", "Fenchel"), False),
    (("Feta",), False),
    (("Fett", "Fette"), False),
    (("Fettuccine",), False),
    (("Filet", "Filets"), False),
    (("Fisch", "Fische"), False),
    (("Fischfilet", "Fischfilets"), False),
    (("Fischkonserve", "Fischkonserven"), False),
    (("Fischstäbchen", "Fischstäbchen"), False),
    (("Fischsuppe",), False),
    (("Fladenbrot", "Fladenbrote"), False),
    (("Flammkuchen", "Flammkuchen"), False),
    (("Flädlisuppe",), False),
    (("Fleckerlsuppe",), False),
    (("Fleischbrühe", "Fleischbrühen"), False),
    (("Fleischkonserve", "Fleischkonserve"), False),
    (("Fleischsuppe",), False),
    (("Fliederbeere", "Fliederbeere"), True),
    (("Fliederbeersuppe",), False),
    (("Florentiner", "Florentiner"), False),
    (("Foie gras",), False),
    (("Frankfurter", "Frankfurter"), False),
    (("Frischkäse", "Frischkäse"), False),
    (("Frittatensuppe",), False),
    (("Frozen Yogurt",), False),
    (("Frucht", "Früchte"), True),
    (("Fruchtbonbon", "Fruchtbonbons"), True),
    (("Fruchteis",), False),
    (("Fruchtjoghurt",), False),
    (("Früchtebrot", "Früchtebrote"), False),
    (("Früchtequark",), False),
    (("Frühlingsrolle", "Frühlingsrollen"), False),
    (("Frühlingssuppe",), False),
    (("Frühlingszwiebel", "Frühlingszwiebeln"), False),
    (("Frühstücksbrot", "Frühstücksbrote"), False),
    (("Garnele", "Garnelen"), False),
    (("Gebäck",), False),
    (("Gehacktes",), False),
    (("Gelée", "Gelées"), False),
    (("Gemüsesuppe",), False),
    (("Gemüsezwiebel",), False),
    (("Gerste", "Gersten"), False),
    (("Gerstensuppe",), False),
    (("Getreide", "Getreide"), False),
    (("Gewürz", "Gewürze"), False),
    (("Gewürzgurke", "Gewürzgurken"), True),
    (("Gorgonzola",), False),
    (("Gouda",), False),
    (("Graupe", "Graupen"), False),
    (("Graupensuppe",), False),
    (("Greyerzer", "Greyerzer"), False),
    (("Grieß", "Grieße"), False),
    (("Grießbrei",), False),
    (("Grießkloß",), False),
    (("Grießklößchen",), False),
    (("Grießknödel",), False),
    (("Grießmehl",), False),
    (("Grießnockerl",), False),
    (("Grießpudding",), False),
    (("Grießschmarren",), False),
    (("Grießsuppe",), False),
    (("Grünkohl",), False),
    (("Gulasch", "Gulasche"), False),
    (("Gulaschsuppe",), False),
    (("Gurke", "Gurken"), False),
    (("Gurkensalat",), False),
    (("Gyros", "Gyros"), False),
    (("Hackepeter",), False),
    (("Hackfleisch",), False),
    (("Hafer", "Hafer"), False),
    (("Haferflocken",), False),
    (("Hagebutte", "Hagebutten"), False),
    (("Haifischflossensuppe",), False),
    (("Hartkäse", "Hartkäse"), False),
    (("Harzer",), False),
    (("Haselnuss", "Haselnüsse"), True),
    (("Hefe", "Hefen"), False),
    (("Hefezopf",), False),
    (("Heidelbeere", "Heidelbeeren"), True),
    (("Hering", "Heringe"), True),
    (("Heringssalat",), False),
    (("Hibiskustee",), False),
    (("Himbeere", "Himbeeren"), True),
    (("Himbeereis",), False),
    (("Hirse", "Hirsen"), False),
    (("Holunderblütensirup",), False),
    (("Honig", "Honige"), False),
    (("Honigkuchen", "Honigkuchen"), False),
    (("Honigmelone",), False),
    (("Hummer", "Hummer"), False),
    (("Hummersuppe",), False),
    (("Hummus",), False),
    (("Hühnerfleisch",), False),
    (("Imkerhonig",), False),
    (("Ingwer", "Ingwer"), False),
    (("Instantnudeln",), False),
    (("Instantsuppe",), False),
    (("Irish Stew",), False),
    (("Jagdwurst",), False),
    (("Jägerschnitzel", "Jägerschnitzel"), False),
    (("Jägersuppe",), False),
    (("Joghurt", "Joghurts"), False),
    (("Johannisbeere", "Johannisbeeren"), True),
    (("Johannisbrot", "Johannisbrote"), False),
    (("Julienne",), False),
    (("Juliennesuppe",), False),
    (("Kakaopulver",), False),
    (("Kaki", "Kakis"), False),
    (("Kaltschale", "Kaltschalen"), False),
    (("Kandis",), False),
    (("Kandiszucker",), False),
    (("Karamell",), False),
    (("Karamellbonbon", "Karamellbonbons"), True),
    (("Kardamom",), False),
    (("Karotte", "Karotten"), True),
    (("Kartoffel", "Kartoffeln"), True),
    (("Kartoffelchip", "Kartoffelchips"), True),
    (("Kartoffelsuppe",), False),
    (("Käse", "Käse"), False),
    (("Käsebrötchen",), False),
    (("Käsekuchen",), False),
    (("Keks", "Kekse"), True),
    (("Kirsche", "Kirschen"), True),
    (("Kiwi", "Kiwis"), True),
    (("Knoblauch",), False),
    (("Knoblauchbutter",), False),
    (("Knoblauchöl", "Knoblauchöle"), False),
    (("Knoblauchpulver",), False),
    (("Knoblauchsalz", "Knoblauchsalze"), False),
    (("Knoblauchsauce", "Knoblauchsaucen"), False),
    (("Knoblauchwurst", "Knoblauchwürste"), False),
    (("Kohl",), False),
    (("Kohlroulade", "Kohlrouladen"), False),
    (("Koriander",), False),
    (("Krakauer", "Krakauern"), False),
    (("Krankensuppe",), False),
    (("Krapfen", "Krapfen"), False),
    (("Kraut", "Kräuter"), False),
    (("Kräuterbutter",), False),
    (("Kräuterkäse",), False),
    (("Krebsfleisch",), False),
    (("Krebssuppe",), False),
    (("Kreuzkümmel", "Kreuzkümmel"), False),
    (("Kuchen", "Kuchen"), False),
    (("Kurkuma", "Kurkumen"), False),
    (("Kümmel", "Kümmel"), False),
    (("Kürbis", "Kürbisse"), False),
    (("Kürbiskern", "Kürbiskerne"), True),
    (("Kürbiskernbrot", "Kürbiskernbrote"), False),
    (("Kürbissuppe",), False),
    (("Labskaus",), False),
    (("Lachs", "Lachse"), False),
    (("Lakritz", "Lakritze"), False),
    (("Lammfleisch",), False),
    (("Languste", "Langusten"), False),
    (("Lasagne", "Lasagnen"), False),
    (("Lauch", "Lauche"), False),
    (("Lauchzwiebel",), False),
    (("Leberkäse", "Leberkäse"), False),
    (("Leberwurst", "Leberwürste"), False),
    (("Lebkuchen", "Lebkuchen"), False),
    (("Lebkuchengewürz",), False),
    (("Limburger",), False),
    (("Limette", "Limetten"), False),
    (("Linguine",), False),
    (("Linse", "Linsen"), True),
    (("Linsensuppe",), False),
    (("Lorbeerblatt", "Lorbeerblätter"), False),
    (("Magermilchpulver",), False),
    (("Mais",), False),
    (("Maisgrieß", "Maisgrieße"), False),
    (("Maiskolben", "Maiskolben"), False),
    (("Maismehl",), False),
    (("Majoran"), False),
    (("Mandarine", "Mandarinen"), True),
    (("Mandel", "Mandeln"), False),
    (("Mandelkern", "Mandelkerne"), True),
    (("Mango", "Mangos"), False),
    (("Mangomousse",), False),
    (("Maniok",), False),
    (("Maracuja", "Maracujas"), False),
    (("Margarine",), False),
    (("Marmelade",), False),
    (("Marmorkuchen",), False),
    (("Marzipan",), False),
    (("Mascarpone",), False),
    (("Matcha",), False),
    (("Maultaschen",), False),
    (("Meerrettich",), False),
    (("Mehl",), False),
    (("Melone", "Melonen"), False),
    (("Mett",), False),
    (("Mettwurst", "Mettwürste"), False),
    (("Milchpulver", "Milchpulver"), False),
    (("Milchreis", "Milchreise"), False),
    (("Milchsuppe",), False),
    (("Miso",), False),
    (("Mohn",), False),
    (("Mohnbrötchen", "Mohnbrötchen"), False),
    (("Mozzarella", "Mozzarellas"), False),
    (("Möhre", "Möhren"), True),
    (("Mus", "Muse"), False),
    (("Müsli", "Müsli"), False),
    (("Nektarinen",), False),
    (("Nockerl",), False),
    (("Nockerlsuppe",), False),
    (("Noisette",), False),
    (("Noisetteschokolade",), False),
    (("Nudeln",), False),
    (("Nugat", "Nugats"), False),
    (("Nuss", "Nüsse"), False),
    (("Nusskuchen",), False),
    (("Nussschinken",), False),
    (("Nussschokolade",), False),
    (("Nutella",), False),
    (("Oberländer",), False),
    (("Obst",), False),
    (("Obstkuchen",), False),
    (("Okroschka",), False),
    (("Olive", "Oliven"), True),
    (("Olivenöl", "Olivenöle"), False),
    (("Omelett", "Omelette"), False),
    (("Orange", "Orangen"), True),
    (("Orangeat",), False),
    (("Oregano",), False),
    (("Pampelmuse", "Pampelmusen"), True),
    (("Panadelsuppe",), False),
    (("Paprika", "Paprikas"), False),
    (("Paranuss", "Paranüsse"), True),
    (("Parmesankäse",), False),
    (("Pasta",), False),
    (("Pastete", "Pasteten"), False),
    (("Pastinake", "Pastinaken"), True),
    (("Pecannuss", "Pecannüsse"), False),
    (("Peperoni", "Peperoni"), False),
    (("Persillade",), False),
    (("Pesto",), False),
    (("Petersilie", "Petersilien"), False),
    (("Pfannkuchen", "Pfannkuchen"), False),
    (("Pfeffer", "Pfeffer"), False),
    (("Pfefferkuchen",), False),
    (("Pferdefleisch",), False),
    (("Pfifferling", "Pfifferlinge"), False),
    (("Pfirsich", "Pfirsiche"), False),
    (("Pflaume", "Pflaumen"), True),
    (("Pilz", "Pilze"), True),
    (("Pilzsuppe",), False),
    (("Piment", "Pimente"), False),
    (("Pinienkern", "Pinienkerne"), True),
    (("Pistazie", "Pistazien"), True),
    (("Pita", "Pitas"), False),
    (("Pizza", "Pizzen"), False),
    (("Plätzchen", "Plätzchen"), False),
    (("Polenta",), False),
    (("Pommes frites"), False),
    (("Pommes", "Pommes"), False),
    (("Porridge",), False),
    (("Posaunensuppe",), False),
    (("Preiselbeere", "Preiselbeeren"), True),
    (("Puderzucker",), False),
    (("Puffreis",), False),
    (("Pumpernickel", "Pumpernickel"), False),
    (("Putenfleisch",), False),
    (("Quark",), False),
    (("Quarkbällchen",), False),
    (("Quarktasche", "Quarktaschen"), False),
    (("Quiche", "Quiches"), False),
    (("Quitte", "Quitten"), False),
    (("Radicchio",), False),
    (("Radieschen", "Radieschen"), False),
    (("Rahm",), False),
    (("Rahmsuppe",), False),
    (("Ramen",), False),
    (("Ravioli", "Raviolis"), False),
    (("Räucherlachs", "Räucherlachse"), False),
    (("Reis", "Reise"), False),
    (("Reissuppe",), False),
    (("Remoulade", "Remouladen"), False),
    (("Rettich", "Rettiche"), False),
    (("Rhabarber", "Rhabarber"), False),
    (("Ricotta",), False),
    (("Rinderroulade",), False),
    (("Rindfleisch",), False),
    (("Rindfleischsuppe",), False),
    (("Roggen", "Roggen"), False),
    (("Roggenbrot", "Roggenbrote"), False),
    (("Rohkost",), False),
    (("Rohrzucker",), False),
    (("Rollmops",), False),
    (("Romadur",), False),
    (("Rosenkohl", "Rosenkohle"), False),
    (("Rosine", "Rosinen"), False),
    (("Rosinenkuchen", "Rosinenkuchen"), False),
    (("Rosinenschnecke", "Rosinenschnecken"), False),
    (("Rosmarin",), False),
    (("Rote Beete",), False),
    (("Rotkohl",), False),
    (("Rotkraut",), False),
    (("Rotschimmelkäse",), False),
    (("Rotwein", "Rotweine"), False),
    (("Rucola",), False),
    (("Rumfordsuppe",), False),
    (("Rumkugel", "Rumkugeln"), False),
    (("Rübe", "Rüben"), False),
    (("Rübenkraut",), False),
    (("Rübenzucker",), False),
    (("Salami", "Salami"), False),
    (("Salatgurke", "Salatgurken"), False),
    (("Salbei",), False),
    (("Salz", "Salze"), False),
    (("Salzbrezel",), False),
    (("Salzgurke", "Salzgurken"), True),
    (("Salzstange", "Salzstangen"), False),
    (("Sardelle", "Sardellen"), False),
    (("Sauerkraut",), False),
    (("Sauermilch",), False),
    (("Sauermilchquark",), False),
    (("Sauerrahm",), False),
    (("Schafskäse",), False),
    (("Schalotte", "Schalotten"), False),
    (("Schinken", "Schinken"), False),
    (("Schleimsuppe",), False),
    (("Schmorbraten", "Schmorbraten"), False),
    (("Schnittlauch", "Schnittlauche"), False),
    (("Schokolade", "Schokoladen"), False),
    (("Schwalbennestersuppe",), False),
    (("Schwarzbrot", "Schwarzbrote"), False),
    (("Schwarzkümmel",), False),
    (("Schwarzwälder Schinken",), False),
    (("Schwarzwurzel", "Schwarzwurzeln"), False),
    (("Schweinefleisch",), False),
    (("Seitan",), False),
    (("Sellerie", "Selleries"), False),
    (("Senf", "Senfe"), False),
    (("Senfgurke", "Senfgurken"), True),
    (("Sesam", "Sesame"), False),
    (("Sesambrötchen",), False),
    (("Sesamsauce", "Sesamsaucen"), False),
    (("Soja", "Sojen"), False),
    (("Sojasprossen",), False),
    (("Sonnenblumenkern", "Sonnenblumenkerne"), True),
    (("Spaghetti", "Spaghetti"), False),
    (("Spargel", "Spargel"), False),
    (("Spargelsuppe",), False),
    (("Spätzle",), False),
    (("Spekulatius", "Spekulatius"), False),
    (("Spinat", "Spinate"), False),
    (("Spritzgebäck",), False),
    (("Steinpilz", "Steinpilze"), True),
    (("Sternanis",), False),
    (("Stollen", "Stollen"), False),
    (("Stracciatella", "Stracciatelle"), False),
    (("Stutenmilch",), False),
    (("Suppenextrakt", "Suppenextrakte"), False),
    (("Suppenfleisch", "Suppenfleische"), False),
    (("Suppengrün",), False),
    (("Suppenhuhn", "Suppenhühner"), False),
    (("Suppenknochen",), False),
    (("Suppenspargel", "Suppenspargeln"), False),
    (("Suppenwürfel",), False),
    (("Sushi", "Sushi"), False),
    (("Süßkartoffel", "Süßkartoffeln"), False),
    (("Süßrahm",), False),
    (("Süßrahmbutter",), False),
    (("Tagessuppe",), False),
    (("Tagliatelle", "Tagliatelles"), False),
    (("Tahin",), False),
    (("Tamarinde", "Tamarinden"), False),
    (("Tapioka", "Tapiokas"), False),
    (("Teewurst", "Teewürste"), False),
    (("Tellerfleisch",), False),
    (("Tempeh",), False),
    (("Terrine", "Terrinen"), False),
    (("Tiefkühlkost",), False),
    (("Tiefkühlpizza", "Tiefkühlpizzas"), False),
    (("Tilsiter", "Tilsiter"), False),
    (("Tiramisu", "Tiramisus"), False),
    (("Toast", "Toaste"), False),
    (("Tofu", "Tofus"), False),
    (("Tomate", "Tomaten"), False),
    (("Tomatenmark", "Tomatenmarke"), False),
    (("Tomatensoße", "Tomatensoßen"), False),
    (("Tomatensuppe",), False),
    (("Topinambur", "Topinamburen"), False),
    (("Tortellini", "Tortellinis"), False),
    (("Traube", "Trauben"), True),
    (("Traubenkernöl", "Traubenkernöle"), False),
    (("Urbrot", "Urbrote"), False),
    (("Vanille",), False),
    (("Vanillekipferl",), False),
    (("Vanillepudding", "Vanillepuddinge"), False),
    (("Vanillerostbraten",), False),
    (("Vanillezucker",), False),
    (("Vanillinzucker",), False),
    (("Vollkornbrot", "Vollkornbrote"), False),
    (("Vollkornmehl",), False),
    (("Vollmilchpulver",), False),
    (("Vollmilchschokolade",), False),
    (("Vollrohrzucker",), False),
    (("Walnuss", "Walnüsse"), False),
    (("Wasabi", "Wasabi"), False),
    (("Wassermelone", "Wassermelonen"), False),
    (("Wassersuppe",), False),
    (("Weichkäse", "Weichkäse"), False),
    (("Weihnachtsgebäck",), False),
    (("Weintraube", "Weintrauben"), True),
    (("Weißbrot", "Weißbrote"), False),
    (("Weißkohl",), False),
    (("Weißkraut",), False),
    (("Weißschimmelkäse",), False),
    (("Weißwein", "Weißweine"), False),
    (("Weizen",), False),
    (("Weizengrieß",), False),
    (("Weizenmehl",), False),
    (("Wirsing", "Wirsinge"), False),
    (("Wurst", "Würste"), False),
    (("Wurstbrühe",), False),
    (("Wurstsuppe",), False),
    (("Xylit",), False),
    (("Yoghurt", "Yoghurte"), False),
    (("Zander", "Zander"), False),
    (("Zaziki", "Zazikis"), False),
    (("Ziegenkäse",), False),
    (("Ziegenmilch",), False),
    (("Zimt",), False),
    (("Zimtstange", "Zimtstangen"), False),
    (("Zitronat", "Zitronate"), False),
    (("Zitrone", "Zitronen"), False),
    (("Zitronensaft", "Zitronensäfte"), False),
    (("Zucchini", "Zucchini"), False),
    (("Zucker", "Zucker"), False),
    (("Zuckerguss",), False),
    (("Zuckerrübensirup",), False),
    (("Zwiebel", "Zwiebeln"), False),
    (("Zwiebelkuchen", "Zwiebelkuchen"), False),
    (("Zwiebelring", "Zwiebelringe"), False),
    (("Zwiebelsuppe",), False),
    (("Öl", "Öle"), False),
    (("Überraschungsei", "Überraschungseier"), True),
]


ACTION = [
    "ablöschen",
    "abreiben",
    "anbraten",
    "aufkochen",
    "auskochen",
    "backen",
    "blanchieren",
    "blind backen",
    "braisieren",
    "braten",
    "dressieren",
    "dämpfen",
    "dünsten",
    "entkernen",
    "entsteinen",
    "filetieren",
    "frittieren",
    "füllen",
    "garen",
    "gelieren",
    "glasieren",
    "gratinieren",
    "grillen",
    "legieren",
    "marinieren",
    "mixen",
    "panieren",
    "passieren",
    "pasteurisieren",
    "pochieren",
    "poelieren",
    "pürieren",
    "reduzieren",
    "rösten",
    "rüsten",
    "sautieren",
    "schmoren",
    "schälen",
    "sieden",
    "steamen",
    "stopfen",
    "süssen",
    "toasten",
    "tranchieren",
    "verfeinern",
    "waschen",
    "würzen",
    "ziehen lassen",
]

# Pluralize with wiktionary:
# from wiktionaryparser import WiktionaryParser
# parser = WiktionaryParser()
# parser.set_default_language('german')
# not_found = []
# for food in FOOD:
#     try:
#         plural = re.search('(?<=plural )([a-zA-ZäöüßÄÖÜ]*)', parser.fetch(food)[0]["definitions"][0]["text"][0]).groups()[0]
#         print(f'("{food}", "{plural}"),')
#     except Exception as e:
#         print(f'("{food}",),')
#         not_found.append((food, e))