test = {
  'name': 'smallest-int',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int;
          4/17/2019 10:19:17|4
          4/19/2019 17:46:44|4
          4/20/2019 20:29:22|5
          4/16/2019 18:44:34|6
          4/17/2019 9:44:12|6
          4/16/2019 16:16:24|7
          4/16/2019 16:52:00|7
          4/17/2019 10:13:42|7
          4/17/2019 9:40:49|7
          4/17/2019 9:41:06|7
          4/17/2019 11:35:47|8
          4/16/2019 17:26:09|10
          4/16/2019 16:19:04|11
          4/17/2019 10:15:49|13
          4/16/2019 18:18:54|14
          4/16/2019 16:19:13|17
          4/17/2019 10:11:35|17
          4/17/2019 9:43:01|19
          4/20/2019 13:33:12|19
          4/17/2019 10:12:51|31
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab11.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
