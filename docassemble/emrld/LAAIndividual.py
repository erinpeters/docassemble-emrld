from docassemble.base.util import Individual, DAObject, Value

class LAAIndividual(Individual):
  def init(self, *pargs, **kwargs):
    self.initializeAttribute('annual_income', Value)
    self.initializeAttribute('monthly_income', Value)
    self.initializeAttribute('assets', Value)
    super(LAAIndividual, self).init(*pargs, **kwargs)