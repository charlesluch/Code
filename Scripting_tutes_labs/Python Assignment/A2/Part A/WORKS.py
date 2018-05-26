#! usr/bin/env python3

# running from JSONDecodeError: Extra data, Attribute error, Expecting double quotes...
# we need services as a dictionary and flows as an array...

    with open(realConfig, 'r') as c:
        data = c.read().replace('\n','')
        jConfig = json.dumps('"{}"'.format(data))
        print(jConfig)

# we were just printing the string with wierd added \ characters...

    with open(realConfig, 'r') as c:
        data = c.read().replace('\n','')
        print(data)

# .json is now valid, turns out it was an encoding problem, we needed also to use json.load

    with io.open(realConfig, 'r', encoding='utf8') as c:
        plan = json.load(c)
        print(c)
        print(plan)

        # we can now call by key as follows:
        print(plan['flows']['Append at morning'])

    # accessing json file instructions...
    for flow in plan['flows']:
        print("\nFlow is:", flow)
        for service in plan['flows'][flow]:
            print("\tcalling service:", service)
            params = plan['services'][service]

            # open the service and run the external program
            command = [params]
            print(command)
            p = run(command, stdout=PIPE, input='', encoding='utf-8')
            print(p.returncode)
            print(p.stdout)
