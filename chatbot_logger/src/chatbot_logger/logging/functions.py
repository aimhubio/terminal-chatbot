from .chat import Release, Experiment


def get_release_by_version(version: str):
    try:
        release = Release.filter(f'c.version == "{version}"').first()
        return {
            'hash': release.hash,
            'params': release[...],
            'container_type': release.get_typename(),
            'container_full_type': release.get_full_typename(),
        }
    except StopIteration:
        return None


def get_last_experiment(version):
    try:
        exp = sorted(Experiment.filter(f'c.version == "{version}"'), key=lambda x: x['started'])[0]
        return {
            'hash': exp.hash,
            'params': exp[...],
            'container_type': exp.get_typename(),
            'container_full_type': exp.get_full_typename(),
        }
    except IndexError:
        return None
