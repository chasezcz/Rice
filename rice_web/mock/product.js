export default [
  {
    url: '/product/all',
    type: 'get',
    response: _ => {
      var products = [
        {
          "label": "青岛啤酒",
          "status": "ON_SALE",
          "owned_number": 5020,
          "last_supple_date": "2019-05-04 12:00:00",
          "stardand_price": 20
        },
        {
          "label": "青岛啤酒3",
          "status": "ON_SALE",
          "owned_number": 50320,
          "last_supple_date": "2019-05-04 12:00:00",
          "stardand_price": 203
        },
      ]
      return {
          code: 20000,
          data: products
      }
    }
  },
  {
    url: '/product/add',
    type: 'POST',
    response: _ => {
      return {
        code: 20000,
        data: ''
      }
    }
  }
]
