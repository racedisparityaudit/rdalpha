class CreateMeasureAverages < ActiveRecord::Migration[5.0]
  def change
    create_table :measure_averages do |t|
      t.string :uri
      t.string :value
      t.string :subgroup_name
      t.string :group_name
      t.string :national_value
      t.integer :taxonomy_level_id
      t.timestamps
    end

    remove_column :taxonomy_levels, :white
    remove_column :taxonomy_levels, :mixed
    remove_column :taxonomy_levels, :asian
    remove_column :taxonomy_levels, :black
    remove_column :taxonomy_levels, :chinese
    remove_column :taxonomy_levels, :national

  end
end
