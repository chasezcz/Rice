export default [
  {
    url: '/worker/all',
    type: 'get',
    response: _ => {
      var workers = [
        {
          "name": "青岛啤酒",
          "status": "ON",
          "owned_number": 5020,
          "last_work_date": "2019-05-04 12:00:00",
          "stardand_price": 20
        },
        {
          "name": "青岛啤酒3",
          "status": "OFF",
          "owned_number": 50320,
          "last_work_date": "2019-05-04 12:00:00",
        },
      ]
      return {
          code: 20000,
          data: workers
      }
    }
  },
  {
    url: '/worker/add',
    type: 'POST',
    response: _ => {
      return {
        code: 20000,
        data: null
      }
    }
  }
]
