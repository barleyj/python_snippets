from math import ceil

from pygraphviz import *


dependencies = AGraph()


class DependencyMeta(type):
    def __new__(cls, name, parents, dct):
        # if 'count' not in dct:
        #     dct['count'] = 1

        if 'name' not in dct:
            dct['name'] = name

        if 'acquired' not in dct:
            dct['acquired'] = []

        if 'parent_of' not in dct:
            dct['parent_of'] = []


        for p in dct['parent_of']:
            dependencies.add_edge(dct['name'], p.name, label='Subsidiary')
            if 'shape' in dir(p):
                node = dependencies.get_node(p.name)
                node.attr['shape'] = p.shape
            
        for p in dct['acquired']:
            dependencies.add_edge(dct['name'], p.name, label='Acquired')
            if 'shape' in dir(p):
                node = dependencies.get_node(p.name)
                node.attr['shape'] = p.shape

        return super(DependencyMeta, cls).__new__(cls, name, parents, dct)


class Entity(object):
    __metaclass__ = DependencyMeta


class Company(Entity):
    shape = 'house'

class Employee(Entity):
    shape = 'circle'


class Hand(Company):
    name = '@Hand'

class HawkEyeAP(Company):
    pass

class SenSageAP(Company):
    name = 'SenSage AP'
    

class Crossover(Company):
    pass


class AureaEnergySolutions(Company):
    pass


class GCE(Company):
    pass


class GenSym(Company):
    pass


class Nextance(Company):
    pass

class Exinda(Company):
    pass

class EngineYard(Company):
    pass

class RoseASP(Company):
    pass

class InfobrightIEE(Company):
    pass

class KerioTechnologies(Company):
    pass

class CyberlinkASP(Company):
    acquired = [RoseASP]

class ThinkVine(Company):
    pass

class Jive(Company):
    pass

class WaveSystems(Company):
    acquired = [Jive]

class Conarc(Company):
    pass

class EPMLive(Company):
    pass

class Compressus(Company):
    pass

class QuantumRetail(Company):
    pass

class Lyris(Company):
    pass

class Nextdocs(Company):
    pass

class GFI(Company):
    acquired = [KerioTechnologies, Exinda]

class Hipcricket(Company):
    pass

class MessageOne(Company):
    pass

class Spiral(Company):
    pass

class Update(Company):
    pass

class Acorn(Company):
    pass

class NuView(Company):
    pass

class StillSecure(Company):
    pass

class ObjectStore(Company):
    pass


class Ignite(Company):
    acquired = [SenSageAP, ThinkVine, HawkEyeAP, Acorn, NuView, ObjectStore, InfobrightIEE]

class Accept(Company):
    pass

class Prologic(Company):
    pass

class Agentek(Company):
    pass

class RavenFlow(Company):
    pass

class GeoVue(Company):
    pass

class Right90(Company):
    pass

class AutoTrol(Company):
    pass

class Corizon(Company):
    pass

class Infopia(Company):
    pass

class Think3(Company):
    pass

class Metatomix(Company):
    pass

class Triactive(Company):
    pass

class PurchasingNet(Company):
    pass

class Everest(Company):
    pass

class Alterpoint(Company):
    pass

class eCora(Company):
    pass

class TenFold(Company):
    pass

class ETI(Company):
    pass

class Nuvo(Company):
    pass

class Clear(Company):
    pass


class Artemis(Company):
    name = 'Artemis Software'
    acquired = [Accept]


class AureaSoftware(Company):
    name = 'Aurea Software'
    acquired = [AureaEnergySolutions, GCE, Lyris, Update, Spiral, Hipcricket, Nextdocs, EPMLive]


class VersataSoftware(Company):
    name = 'Versata Software, Inc'
    acquired = [Infopia, Think3, TenFold, ETI, Nuvo, Clear, Compressus, QuantumRetail, MessageOne, Hand, Nextance, GenSym, eCora, Alterpoint, Everest, PurchasingNet, Triactive, Metatomix, Corizon, Hand, AutoTrol, Right90, GeoVue, RavenFlow, Agentek, Prologic, Ignite, StillSecure, WaveSystems]


class Trilogy(Company):
    acquired = [VersataSoftware, Artemis]


class Crossover(Company):
    acquired = [EngineYard]


class ESW(Company):
    name = 'ESW Capital'
    acquired = {CyberlinkASP, Conarc, GFI, AureaSoftware
                }


class ScottBrighton(Employee):
    name = 'Scott Brighton'
    employed_by = [AureaSoftware]

dependencies.layout(prog='dot')
dependencies.draw('aurea.png')
