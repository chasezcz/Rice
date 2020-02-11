import Layout from '@/layout'

const warehouseRouter = {
  path: '/warehouse',
  component: Layout,
  redirect: '/warehouse/index',
  name: 'warehouse',
  meta: {
    title: '仓库管理',
    icon: 'tab'
  },
  children: [
    {
      path: 'index',
      component: () => import('@/views/warehouse/index'),
      name: 'warehouseManage',
      meta: { title: '仓库管理主页', noCache: true }
    },
    {
      path: 'deliver',
      component: () => import('@/views/warehouse/deliver'),
      name: 'warehouseAdmin-deliver',
      meta: { title: '发货', noCache: true }
    },
    {
      path: 'statistics',
      component: () => import('@/views/warehouse/statistics'),
      name: 'warehouseAdmin-statistic',
      meta: { title: '今日统计', noCache: true }
    },
    {
      path: 'collect',
      component: () => import('@/views/warehouse/collect'),
      name: 'warehouseAdmin-collect',
      meta: { title: '进货', noCache: true }
    }
  ]
}

export default warehouseRouter
