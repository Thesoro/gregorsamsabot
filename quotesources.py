import quotereqs as q

l = {}
l['Tale Of Two Cities'] = {'orig':"It was the %s of times, it was the %s of times, it was the age of %s, it was the age of %s.", 'reqs':[q.Quotereqs(pos="Adjective", superl="super"), q.Quotereqs(pos="Adjective", superl="super"),q.Quotereqs(pos='Noun',countmatters="no"),q.Quotereqs(pos='Noun',countmatters="no")]}
l['Moby Dick'] = {'orig':"%s me Ishmael.", 'reqs':[q.Quotereqs(pos="Verb")]}
l['A Christmas Carol'] = {'orig':"Marley was %s: to begin with.  There is no %s whatever about that.", 'reqs':[q.Quotereqs(pos="Adjective", superl="not"), q.Quotereqs(pos="Noun", countmatters="no")]}
l['Anna Karenina'] = {'orig':"All %s families are alike; each %s family is %s in its own way.", 'reqs':[q.Quotereqs(pos="Adjective", superl="not"), q.Quotereqs(pos="Adjective", superl="not"), q.Quotereqs(dupe=1)]}
l['Hitchhiker\'s Guide to the Galaxy'] = {'orig':"In the beginning the %s was created. This has made a lot of people very %s and has been widely regarded as %s move.", 'reqs':[q.Quotereqs(pos="Noun"), q.Quotereqs(pos="Adjective", superl="not"), q.Quotereqs(pos="Adjective", superl="not", needsarticle=True)]}
l['The Princess Bride'] = {'orig':"The year that Buttercup was born, the most %s woman in the world was %s %s named %s.", 'reqs':[q.Quotereqs(pos="Adjective", superl="not"), q.Quotereqs(pos="Adjective", superl="not", needsarticle=True), q.Quotereqs(pos='Noun',countmatters="yes"), q.Quotereqs(pos='Proper noun')]}
l['The Long Dark Tea-Time of the Soul'] = {'orig':"It can hardly be a coincidence that no language on Earth has ever produced the phrase, \"as %s as %s\".", 'reqs':[q.Quotereqs(pos="Adjective", superl="not"),q.Quotereqs(pos='Noun',countmatters="yes", needsarticle=True)]}
l['Fear and Loathing in Las Vegas'] = {'orig':"We were somewhere around Barstow on the edge of the %s when the %s began to take hold."}
l['Fear and Loathing in Las Vegas']['reqs'] = [q.Quotereqs(pos="Noun"), q.Quotereqs(pos="Noun", pluralform="True")]
l['Scottish Beth'] = {'orig':"When shall we three meet again / In %s, %s, or in %s?"}
l['Scottish Beth']['reqs'] = [q.Quotereqs(pos="Noun", countmatters="no"), q.Quotereqs(pos="Noun", countmatters="no"), q.Quotereqs(pos="Noun", countmatters="no")]
l['Fahrenheit 451'] = {'orig':"It was %s to burn."}
l['Fahrenheit 451']['reqs'] = [q.Quotereqs(pos="Noun", countmatters="yes", plural="False", needsarticle=True)]
l['Neuromancer'] = {'orig':"The sky above the port was the color of %s, tuned to %s %s."}
l['Neuromancer']['reqs'] = [q.Quotereqs(pos="Noun", countmatters="no"), q.Quotereqs(pos="Adjective", superl="not", needsarticle=True), q.Quotereqs(pos="Noun", countmatters="yes")]
l['Goodfellas'] = {'orig':"As far back as I can remember, I always wanted to be %s."}
l['Goodfellas']['reqs'] = [q.Quotereqs(pos="Noun", countmatters="no", needsarticle=True)]
l['Stand By Me'] = {'orig':"I was 12 going on %s the first time I saw a dead %s."}
l['Stand By Me']['reqs'] = [q.Quotereqs(pos="Noun"),q.Quotereqs(pos="Noun")]
l['Metamorphosis'] = {'orig':"As Gregor Samsa awoke one morning from %s dreams he found himself transformed in his bed into %s %s."}
l['Metamorphosis']['reqs'] = [q.Quotereqs(pos="Adjective", superl="not"),q.Quotereqs(pos="Adjective", needsarticle=True),q.Quotereqs(pos="Noun")]
l['The Stranger'] = {'orig':"Mother died %s. Or maybe, %s; I can't be sure."}
l['The Stranger']['reqs'] = [q.Quotereqs(pos="Adverb"),q.Quotereqs(pos="Adverb")]
l['1984'] = {'orig':"It was a bright %s day in April, and the %s were striking thirteen."}
l['1984']['reqs'] = [q.Quotereqs(pos="Adjective"),q.Quotereqs(pos="Noun", countmatters="yes", pluralform="True")]
l['Pride and Prejudice'] = {'orig':"It is a truth universally acknowledged, that a single man in possession of a good %s, must be in want of %s."}
l['Pride and Prejudice']['reqs'] = [q.Quotereqs(pos="Noun", countmatters="yes"),q.Quotereqs(pos="Noun", countmatters="yes", plural="False", needsarticle=True)]
l['Lolita'] = {'orig':"Lolita, %s of my life, %s of my loins."}
l['Lolita']['reqs'] = [q.Quotereqs(pos="Noun"),q.Quotereqs(pos="Noun")]
