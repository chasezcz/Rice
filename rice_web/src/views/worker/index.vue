<template>
  <div style="padding: 10px 20px 0 20px">
    <div style="padding: 0 0 20px 0">
      <h1>职员数量：{{ list.length }}</h1>
      <el-button type="primary" @click="dialogVisible = true">添加新职员</el-button>
    </div>
    <el-table :data="list" border fit highlight-current-row class="productTable">
      <el-table-column align="center" label="序号">
        <template slot-scope="{row, $index}">
          <span>{{ $index + 1 }}</span>
        </template>
      </el-table-column>

      <el-table-column align="center" label="姓名">
        <template slot-scope="{row}">
          <span>{{ row.name }}</span>
        </template>
      </el-table-column>

      <el-table-column align="center" label="入职时间">
        <template slot-scope="{row}">
          <span>{{ row.register_date | parseTime('{y}-{m}-{d} {h}:{i}') }}</span>
        </template>
      </el-table-column>

      <el-table-column align="center" label="最近一次工作时间">
        <template slot-scope="{row}">
          <span>{{ row.last_work_date | parseTime('{y}-{m}-{d} {h}:{i}') }}</span>
        </template>
      </el-table-column>

      <el-table-column label="状态">
        <template slot-scope="{row}">
          <el-tag :type="row.status | statusFilter">
            {{ row.status | statusFilter2 }}
          </el-tag>
        </template>
      </el-table-column>

      <el-table-column align="center" label="操作">
        <template slot-scope="{row}">
          <el-button
            type="success"
            icon="el-icon-circle-check-outline"
            @click="confirmEdit(row)"
          >
            修改
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog
      title="操作"
      :visible.sync="dialogVisible"
      width="30%"
      :before-close="handleClose"
    >
      <div>
        <el-form ref="workerData" :model="workerData" label-width="100px">
          <el-form-item label="姓名" required>
            <el-input v-model="workerData.name" />
          </el-form-item>
          <el-form-item label="就职时间" required>
            <el-date-picker v-model="workerData.register_date" type="date" placeholder="选择日期" style="width: 100%;" />
          </el-form-item>
          <el-form-item label="最后一次工作时间" required>
            <el-date-picker v-model="workerData.last_work_date" type="date" placeholder="选择日期" style="width: 100%;" />
          </el-form-item>
          <el-radio-group v-model="workerData.status">
            <el-radio label="ON">在职</el-radio>
            <el-radio label="OFF">离职</el-radio>
          </el-radio-group>
        </el-form>
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="handleCreate">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { getAllWorkers, addWorker } from '@/api/worker'
export default {
  filters: {
    statusFilter(status) {
      const statusMap = {
        published: 'ON',
        draft: 'OFF',
        deleted: 'OFF'
      }
      return statusMap[status]
    },
    statusFilter2(status) {
      const statusMap = {
        'ON': '在职',
        'OFF_SALE': '停售',
        'OFF': '离职'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      list: [],
      dialogVisible: false,
      workerData: {}
    }
  },
  created: function() {
    getAllWorkers().then(response => {
      this.list = response.data
    })
  },
  methods: {
    handleCreate(data) {
      addWorker(data).then(response => {
        if (response.code === 20000) {
          this.$message({
            message: '操作成功',
            type: 'success'
          })
        } else {
          this.$message({
            message: '操作失败' + response.data,
            type: 'warning'
          })
        }
      })
    },
    confirmEdit(row) {
      this.workerData = row
      this.dialogVisible = true
    },
    handleClose() {
      this.workerData = {}
      this.dialogVisible = false
    }
  }
}
</script>

<style lang="scss" scoped>
.productTable {
  margin: 0 auto;
  padding: 0 20px 0 20px;
}
</style>
