import Layout from '@/layout'

const productRouter = {
  path: '/product',
  component: Layout,
  redirect: '/product/index',
  name: 'ProductManage',
  meta: {
    title: '产品管理',
    icon: 'tree-table',
    roles: ['admin']
  },
  children: [
    {
      path: 'index',
      component: () => import('@/views/product/index'),
      name: 'productManager',
      meta: { title: '产品管理', noCache: true }
    }
  ]
}

export default productRouter
