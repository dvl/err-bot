
from errbot import BotPlugin, botcmd, arg_botcmd


class Skeleton(BotPlugin):
    """ wrapper for fabric commands """

    def check_configuration(self, configuration):
        try:
            self['PROJECTS']
        except KeyError:
            self['PROJECTS'] = []

        super(Skeleton, self).check_configuration()

    @arg_botcmd('name', dest='name', type=str)
    @arg_botcmd('fabfile', dest='fabfile', type=str)
    def project_add(self, name, fabfile):
        project = {'name': name, 'fabfile': fabfile}

        self['PROJECTS'].append(project)

        return 'Done'

    @botcmd
    def project_remove(self, mess, args):
        # Will respond to !basket remove
        pass

    @botcmd
    def project_list(self, mess, args):
        return self['PROJECTS']

    @arg_botcmd('project', type=str)
    @arg_botcmd('branch', type=str)
    def deploy(self, project, branch):
        yield 'starting deploy...'

        yield 'Deployed {} of project {}'.format(branch, project)
