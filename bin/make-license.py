#!/usr/bin/env python

'''Re-make license file with the right URL.'''


import utils


TEMPLATE = '''---
permalink: /license/
---

All of this site is made available under the Creative Commons Attribution
license. You are free:

-   to Share - to copy, distribute and transmit the work

-   to Remix - to adapt the work

Under the following conditions:

-   Attribution - You must attribute the work using "Copyright © <NAME>" (but
    not in any way that suggests that we endorse you or your use of the work).
    Where practical, you must also include a hyperlink to <URL>.

With the understanding that:

-   Waiver - Any of the above conditions can be waived if you get permission
    from the copyright holder.

-   Other Rights - In no way are any of the following rights affected by the
    license:
    -   Your fair dealing or fair use rights;
    -   The author's moral rights;
    -   Rights other persons may have either in the work itself or in how
        the work is used, such as publicity or privacy rights.

-   Notice - For any reuse or distribution, you must make clear to others the
    license terms of this work. The best way to do this is with a link to
    <http://creativecommons.org/licenses/by/4.0/>.

For the full legal text of this license, please see <http://creativecommons.org/licenses/by/4.0/legalcode>.
'''


def make_license(options):
    '''Main driver.'''
    config = utils.read_yaml(options.config)
    text = TEMPLATE\
        .replace('<URL>', f'<{config["url"]}>')\
        .replace('<NAME>', f'{config["author"]["name"]}')
    with open(options.output, 'w') as writer:
        writer.write(text)


if __name__ == '__main__':
    options = utils.get_options(
        ['--config', False, 'Path to YAML configuration file'],
        ['--output', False, 'Path to output license file']
    )
    make_license(options)
