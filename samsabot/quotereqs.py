class Quotereqs:
  def __init__(self, pos='', needsarticle = '', superl = '', countmatters = '', dupe='', plural='', pluralform=''):
    self.pos = pos

    # multipos requirements
    self.needsarticle = needsarticle

    #adjective
    self.superl = superl

    #noun
    self.countmatters = countmatters
    self.plural = plural
      #gives plural form for unpluralized nouns - "normal" for ones that just add s, the full thing otherwise
    self.pluralform = pluralform

    #duplicates - a number indicates the array position of the word to be duped
    self.dupe = dupe

    self.valuesearchers = [self.superl, self.countmatters, self.plural]
