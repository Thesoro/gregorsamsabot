class Quotereqs:
  def __init__(self, pos='', needsarticle = '', superl = '', countmatters = '', dupe='', plural=''):
    self.pos = pos

    # multipos requirements
    self.needsarticle = needsarticle

    #adjective
    self.superl = superl

    #noun
    self.countmatters = countmatters
    self.plural = plural

    #duplicates - a number indicates the array position of the word to be duped
    self.dupe = dupe

    self.valuesearchers = [self.superl, self.countmatters, self.plural]
