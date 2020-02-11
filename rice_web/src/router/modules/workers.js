import Layout from '@/layout'

const workerRouter = {
  path: '/workerMg',
  component: Layout,
  redirect: '/worker/index',
  name: 'WorkerMg',
  meta: {
    title: '人员管理',
    icon: 'star',
    roles: ['admin']
  },
  children: [
    {
      path: 'index',
      component: () => import('@/views/worker/index'),
      name: 'workerMgIdx',
      meta: { title: '人员管理', noCache: true }
    }
  ]
}

export default workerRouter
