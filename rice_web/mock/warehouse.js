
export default [
  {
    url: '/warehouse/getDeliveryInfo',
    type: 'get',
    response: config => {
      var salers = [
        {
          "label": "张三",
          "value": "张三"
        },
        {
          "label": "李四",
          "value": "李四"
        },
        {
          "label": "王五",
          "value": "王五"
        }
      ]
      // var products = [
      //   {
      //     "label": "青岛啤酒",
      //     "options": [
      //       {
      //         "label": "精品",
      //         "value": "青岛啤酒精品",
      //         "number": 200
      //       },
      //       {
      //         "label": "塑装",
      //         "value": "青岛啤酒塑装",
      //         "number": 200
      //       },
      //       {
      //         "label": "金麦",
      //         "value": "青岛啤酒金麦",
      //         "number": 200
      //       }
      //     ]
      //   },
      //   {
      //     "label": "崂山啤酒",
      //     "options": [
      //       {
      //         "label": "塑装",
      //         "value": "崂山啤酒塑装",
      //         "number": 200
      //       },
      //       {
      //         "label": "包装",
      //         "value": "崂山啤酒包装",
      //         "number": 200
      //       }
      //     ]
      //   },
      //   {
      //     "label": "雪花啤酒",
      //     "options": [
      //       {
      //         "label": "塑装",
      //         "value": "雪花啤酒塑装",
      //         "number": 200
      //       },
      //       {
      //         "label": "包装",
      //         "value": "雪花啤酒包装",
      //         "number": 200
      //       }
      //     ]
      //   }
      // ]
      var products = [
        {
          "label": "份额无法",
          "number": 200
        },
        {
          "label": "凤飞飞",
          "number": 200
        },{
          "label": "份额法",
          "number": 200
        },{
          "label": "俄文法份额",
          "number": 200
        },{
          "label": "为厄俄",
          "number": 200
        },{
          "label": "和研讨会",
          "number": 200
        },{
          "label": "清俄国人",
          "number": 200
        },{
          "label": "内容发表过",
          "number": 200
        },{
          "label": "年回国",
          "number": 200
        },
      ]
      return {
        code: 20000,
        data: {
          "salers": salers,
          "products": products
        }
      }
    }
  },
  {
    url: '/warehouse/delivery',
    type: 'post',
    response: _ => {
      return {
        code: 20000,
        data: 'success'
      }
    }
  },
  {
    url: '/warehouse/collect',
    type: 'post',
    response: _ => {
      return {
        code: 20000,
        data: 'success'
      }
    }
  }
]
